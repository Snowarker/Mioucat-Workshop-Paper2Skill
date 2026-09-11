<#
.SYNOPSIS
    一键重建 Mioucat Workshop PDF 处理虚拟环境（Python 3.10 + marker-pdf 2.x + GPU）
    内置镜像源连通性 + 带宽检测：对每个资产类别（PyPI 包 / PyTorch 索引 / HF / GitHub）
    逐一测速所有候选源，综合延迟与实测下载带宽，选出最快的下载路径。

.DESCRIPTION
    完成以下步骤：
      1. 检测 Python 3.10 解释器并创建 venv
      2. 对 PyPI / PyTorch / HuggingFace / GitHub 各镜像源做连通性(HEAD)与带宽(GET 小文件)检测
      3. 从选出的最快源安装 torch 三件套（CUDA 12.6，版本取自 requirements_frozen.txt）
      4. 从最快 PyPI 源安装其余锁定依赖
      5. 检查并下载 llama.cpp CUDA 12.4 双包（llama-server + cudart DLL），缺失时自动补齐
      6. 调用 manage_models.py 检查并补齐模型
      7. 验证 GPU 加速是否生效

.PARAMETER Python
    指定 Python 3.10 解释器路径（默认自动探测 py -3.10 / python）

.PARAMETER CheckMirrorsOnly
    只检测各镜像源连通性与带宽并输出，不执行构建

.PARAMETER SkipModels
    跳过模型检查步骤

.PARAMETER ForceLlama
    强制重新下载 llama.cpp（即使本地已有）

.EXAMPLE
    .\scripts\setup_venv.ps1 -CheckMirrorsOnly
    .\scripts\setup_venv.ps1
    .\scripts\setup_venv.ps1 -Python "D:\...\Python310\python.exe" -SkipModels

.NOTES
    依赖：Python 3.10.x、curl.exe（Win10 自带）、NVIDIA 驱动（CUDA 12+）
    路径约定：脚本固定在 scripts/ 目录，项目根 = 脚本目录的父目录；
    所有文件（venv、requirements_frozen.txt、models、tools）均相对项目根定位，
    从任意工作目录运行本脚本均有效。
#>
param(
    [string]$Python,
    [switch]$CheckMirrorsOnly,
    [switch]$SkipModels,
    [switch]$ForceLlama
)

$ErrorActionPreference = "Stop"
# 路径全部相对脚本自身定位：脚本固定在 scripts/ 下，项目根为其父目录
# 从任意工作目录运行均可正常工作
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = Split-Path -Parent $ScriptDir
Set-Location $Root

function Write-Step { param($Msg) Write-Host "`n=== $Msg ===" -ForegroundColor Cyan }
function Write-Ok   { param($Msg) Write-Host "  [OK] $Msg" -ForegroundColor Green }
function Write-Warn { param($Msg) Write-Host "  [!] $Msg" -ForegroundColor Yellow }
function Write-Fail { param($Msg) Write-Host "  [FAIL] $Msg" -ForegroundColor Red }

# ---------------------------------------------------------------
# 1. 镜像源清单（含常见但可能不可达的源，检测结果如实显示）
# ---------------------------------------------------------------
$PyPIMirrors = @(
    @{ Name = "PyPI 官方";      Url = "https://pypi.org/simple/" },
    @{ Name = "清华 TUNA";      Url = "https://pypi.tuna.tsinghua.edu.cn/simple/" },
    @{ Name = "阿里云";          Url = "https://mirrors.aliyun.com/pypi/simple/" },
    @{ Name = "中科大 USTC";    Url = "https://pypi.mirrors.ustc.edu.cn/simple/" },
    @{ Name = "腾讯云";          Url = "https://mirrors.cloud.tencent.com/pypi/simple/" },
    @{ Name = "华为云";          Url = "https://repo.huaweicloud.com/repository/pypi/simple/" },
    @{ Name = "豆瓣(douban)";   Url = "https://pypi.douban.com/simple/" },
    @{ Name = "北外 BFSU";      Url = "https://mirrors.bfsu.edu.cn/pypi/web/simple/" },
    @{ Name = "南大 NJU";       Url = "https://mirror.nju.edu.cn/pypi/web/simple/" },
    @{ Name = "浙大 ZJU";       Url = "https://mirrors.zju.edu.cn/pypi/web/simple/" },
    @{ Name = "哈工大 HIT";     Url = "https://mirrors.hit.edu.cn/pypi/web/simple/" }
)
$TorchMirrors = @(
    @{ Name = "PyTorch 官方";   Url = "https://download.pytorch.org/whl/cu126" },
    @{ Name = "上海交大 SJTU";  Url = "https://mirror.sjtu.edu.cn/pytorch-wheels/cu126" },
    @{ Name = "阿里云 PyTorch"; Url = "https://mirrors.aliyun.com/pytorch-wheels/cu126" },
    @{ Name = "清华 TUNA";      Url = "https://mirrors.tuna.tsinghua.edu.cn/pytorch-wheels/cu126" }
)
$HFMirrors = @(
    @{ Name = "HF 官方";       Url = "https://huggingface.co" },
    @{ Name = "hf-mirror";     Url = "https://hf-mirror.com" }
)
$GithubMirrors = @(
    @{ Name = "GitHub 官方";   Url = "https://github.com" },
    @{ Name = "gh-proxy";      Url = "https://gh-proxy.com" },
    @{ Name = "ghfast.top";    Url = "https://ghfast.top" },
    @{ Name = "ghproxy.net";   Url = "https://ghproxy.net" },
    @{ Name = "ghproxy.mirrors"; Url = "https://mirror.ghproxy.com" }
)

# ---------------------------------------------------------------
# 2. 检测函数：HEAD 延迟 + GET 小文件实测带宽
# ---------------------------------------------------------------
function Measure-SourceLatency {
    param($Name, $Url)
    try {
        $sw = [System.Diagnostics.Stopwatch]::StartNew()
        $resp = Invoke-WebRequest -Uri $Url -Method Head -TimeoutSec 6 -UseBasicParsing -ErrorAction Stop
        $sw.Stop()
        if ($resp.StatusCode -ge 200 -and $resp.StatusCode -lt 400) {
            return [pscustomobject]@{ Name = $Name; Url = $Url; Ms = $sw.ElapsedMilliseconds; Ok = $true }
        }
    } catch { }
    return [pscustomobject]@{ Name = $Name; Url = $Url; Ms = [int]::MaxValue; Ok = $false }
}

function Measure-Bandwidth {
    # 从镜像下载一个索引小文件，实测下载带宽 (KB/s)；失败返回 0
    param($BaseUrl, $ProbePath)
    try {
        $url = "$BaseUrl/$ProbePath"
        $sw = [System.Diagnostics.Stopwatch]::StartNew()
        $resp = Invoke-WebRequest -Uri $url -Method Get -TimeoutSec 10 -UseBasicParsing -ErrorAction Stop
        $sw.Stop()
        $bytes = $resp.RawContentLength
        if ($bytes -gt 0 -and $sw.Elapsed.TotalSeconds -gt 0) {
            return [math]::Round($bytes / 1024 / $sw.Elapsed.TotalSeconds, 1)
        }
    } catch { }
    return 0
}

function Select-Fastest {
    param($Sources, [string]$Label, [string]$ProbePath = "")
    Write-Host "  -- $Label --"
    $results = @()
    foreach ($s in $Sources) {
        $r = Measure-SourceLatency $s.Name $s.Url
        $kbps = 0
        if ($r.Ok -and $ProbePath) { $kbps = Measure-Bandwidth $r.Url $ProbePath }
        $r | Add-Member -NotePropertyName Kbps -NotePropertyValue $kbps
        $results += $r
        if ($r.Ok) {
            $bw = if ($kbps -gt 0) { " 带宽 {0} KB/s" -f $kbps } else { "无带宽探测" }
            Write-Host ("     [{0,-4}] {1,-16} -> 延迟 {2,6} ms  {3}" -f "OK", $r.Name, $r.Ms, $bw) -ForegroundColor Green
        } else {
            Write-Host ("     [XX]   {0,-16} -> 不可达" -f $r.Name) -ForegroundColor DarkGray
        }
    }
    # 排序：带宽优先（大在前），同带宽比延迟（小在前）
    return ($results | Where-Object { $_.Ok } | Sort-Object @{ E = { $_.Kbps }; Descending = $true }, @{ E = { $_.Ms } } | Select-Object -First 1)
}

# ---------------------------------------------------------------
# 3. 检测 Python 3.10
# ---------------------------------------------------------------
function Get-Python310 {
    if ($Python -and (Test-Path $Python)) { return $Python }
    foreach ($cand in @("py", "python")) {
        try {
            $ver = & $cand -3.10 -c "import sys; print(sys.version.split()[0])" 2>$null
            if ($LASTEXITCODE -eq 0 -and $ver -match "^3\.10") { return (& $cand -3.10 -c "import sys; print(sys.executable)") }
        } catch { }
    }
    throw "未找到 Python 3.10.x，请用 -Python 参数指定解释器路径"
}

# ---------------------------------------------------------------
# 4. 镜像源检测（pip 类源带真实带宽探测）
# ---------------------------------------------------------------
Write-Step "镜像源连通性与带宽检测"
$pypiFast  = Select-Fastest $PyPIMirrors  "PyPI 镜像（带宽探测: simple/pip/）" "pip/"
$torchFast = Select-Fastest $TorchMirrors "PyTorch 索引（带宽探测: torch/）" "torch/"
$hfFast    = Select-Fastest $HFMirrors    "HuggingFace 镜像" ""
$ghFast    = Select-Fastest $GithubMirrors "GitHub 加速镜像" ""

Write-Host ""
Write-Ok ("PyPI 最快:   {0} (延迟 {1} ms, 带宽 {2} KB/s)" -f $pypiFast.Name, $pypiFast.Ms, $pypiFast.Kbps)
Write-Ok ("Torch 最快:  {0} (延迟 {1} ms, 带宽 {2} KB/s)" -f $torchFast.Name, $torchFast.Ms, $torchFast.Kbps)
Write-Ok ("HF 最快:     {0} ({1} ms)" -f $hfFast.Name, $hfFast.Ms)
Write-Ok ("GitHub 最快: {0} ({1} ms)" -f $ghFast.Name, $ghFast.Ms)

if ($CheckMirrorsOnly) { Write-Host "`n仅检测模式，结束。" -ForegroundColor Yellow; exit 0 }

# ---------------------------------------------------------------
# 5. 创建虚拟环境
# ---------------------------------------------------------------
Write-Step "创建虚拟环境 (venv)"
$pyExe = Get-Python310
Write-Ok "使用解释器: $pyExe"
if (-not (Test-Path "$Root\venv")) {
    & $pyExe -m venv "$Root\venv"
    if ($LASTEXITCODE -ne 0) { throw "创建 venv 失败" }
}
$pip = "$Root\venv\Scripts\python.exe"
& $pip -m pip install --upgrade pip --index-url $pypiFast.Url --quiet
Write-Ok "pip 已升级 (源: $($pypiFast.Name))"

# ---------------------------------------------------------------
# 6. 安装 torch 三件套（CUDA 12.6，独立选源）
# ---------------------------------------------------------------
Write-Step "安装 PyTorch (CUDA 12.6) - 源: $($torchFast.Name)"
$frozen = Get-Content "$Root\requirements_frozen.txt"
$torchPkgs = @($frozen | Where-Object { $_ -match "^torch" })
if ($torchPkgs.Count -eq 0) { throw "requirements_frozen.txt 中未找到 torch 依赖行" }
& $pip install @torchPkgs --index-url $torchFast.Url
if ($LASTEXITCODE -ne 0) { throw "torch 安装失败" }

# ---------------------------------------------------------------
# 7. 安装其余锁定依赖（独立选源）
# ---------------------------------------------------------------
Write-Step "安装其余依赖 ($($frozen.Count - $torchPkgs.Count) 个包) - 源: $($pypiFast.Name)"
$others = @($frozen | Where-Object { $_ -notmatch "^torch" })
$tmpReq = "$env:TEMP\requirements_other_$PID.txt"
Set-Content -Path $tmpReq -Value $others -Encoding UTF8
& $pip install -r $tmpReq --index-url $pypiFast.Url
if ($LASTEXITCODE -ne 0) { throw "依赖安装失败" }
Remove-Item $tmpReq -Force -ErrorAction SilentlyContinue

# ---------------------------------------------------------------
# 8. llama.cpp CUDA 12.4 双包（独立选源：GitHub 或 gh-proxy 加速）
# ---------------------------------------------------------------
Write-Step "llama.cpp CUDA 12.4 运行时"
$llamaDir = "$Root\tools\llama_cpp"
$needLlama = $ForceLlama -or -not ((Test-Path "$llamaDir\llama-server.exe") -and (Test-Path "$llamaDir\cudart64_12.dll"))
if (-not $needLlama) {
    Write-Ok "本地已存在 llama-server.exe + cudart DLL，跳过下载"
} else {
    New-Item -ItemType Directory -Path $llamaDir -Force | Out-Null
    $api = "https://api.github.com/repos/ggml-org/llama.cpp/releases/latest"
    $tag = (Invoke-RestMethod -Uri $api -TimeoutSec 15 -UseBasicParsing).tag_name
    $base = "https://github.com/ggml-org/llama.cpp/releases/download/$tag"
    $mainAsset = "llama-$tag-bin-win-cuda-12.4-x64.zip"
    $cudartAsset = "cudart-llama-bin-win-cuda-12.4-x64.zip"
    foreach ($a in @($mainAsset, $cudartAsset)) {
        $url = "$base/$a"
        if (-not $ghFast.Url.EndsWith("github.com")) { $url = "$($ghFast.Url)/$url" }
        Write-Host "  下载 $a ..."
        & curl.exe -L --retry 3 --connect-timeout 15 -o "$llamaDir\$a" $url
        if ($LASTEXITCODE -ne 0) { throw "下载失败: $url" }
        Expand-Archive "$llamaDir\$a" -DestinationPath "$llamaDir" -Force
        Remove-Item "$llamaDir\$a" -Force
    }
    Write-Ok "llama.cpp $tag 已部署到 tools\llama_cpp"
}

# ---------------------------------------------------------------
# 9. 模型检查（manage_models.py）
# ---------------------------------------------------------------
if (-not $SkipModels) {
    Write-Step "模型检查与补齐"
    & "$pip" "$Root\scripts\manage_models.py"
    if ($LASTEXITCODE -ne 0) { Write-Warn "模型未完全就绪，可稍后重跑 scripts\manage_models.py" }
}

# ---------------------------------------------------------------
# 10. 环境变量与验证
# ---------------------------------------------------------------
Write-Step "环境配置与验证"
$env:MODEL_CACHE_DIR = "$Root\models"
$env:HF_HOME = "$Root\models\hf_home"
$env:SURYA_INFERENCE_BACKEND = "llamacpp"
$env:LLAMA_CPP_BINARY = "$llamaDir\llama-server.exe"
$env:LLAMA_CPP_NGL = "99"
& $pip -c "import torch; print('PyTorch:', torch.__version__, '| CUDA available:', torch.cuda.is_available(), '| GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'N/A')"
Write-Host ""
Write-Ok "环境重建完成！"
Write-Host "  后续使用:  & '.\venv\Scripts\python.exe' scripts\process_pdf.py" -ForegroundColor Cyan
Write-Host "  模型管理:  & '.\venv\Scripts\python.exe' scripts\manage_models.py --check" -ForegroundColor Cyan
Write-Host "  注意: GPU 加速需保持 SURYA_INFERENCE_BACKEND=llamacpp 等环境变量（见 skill 文档）" -ForegroundColor Yellow

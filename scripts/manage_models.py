#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: manage_models.py

Purpose:
    Standalone model directory & version manager for marker/surya 2.x.
    Responsibilities:
      1. Set unified model path environment variables
         (MODEL_CACHE_DIR / HF_HOME / SURYA_GGUF_LOCAL_*).
      2. Inspect local models under the project models/ directory.
      3. Compare against remote latest versions
         (s3 checkpoints are declared by surya settings; HF models are
         compared against the latest repo commit).
      4. Download missing models / update to the newest version.
      5. Print a status report.

Usage:
    python scripts/manage_models.py              # check + auto-download missing (default)
    python scripts/manage_models.py --check      # report only, no download
    python scripts/manage_models.py --update     # force re-check remote and update
    python scripts/manage_models.py --prune      # check + remove stale legacy versions

    process_pdf.py calls `setup_model_env()` and `ensure_models()` from this module.

Virtual Environment:
    Run within the project venv (Python 3.10.11).

Dependencies:
    - surya (2.x, installed in venv)
    - huggingface_hub (installed as marker/surya dependency)

Author:
    MiouCat Workshop
    Date: 2026-09-11
"""

import os
import json
import argparse
from pathlib import Path

# Terminal color codes
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    @staticmethod
    def colorize(text, color):
        return f"{color}{text}{Colors.RESET}"


def get_project_root():
    """Return the project root based on this script's location."""
    return Path(__file__).resolve().parent.parent


def setup_model_env(project_root=None):
    """
    Set all model path environment variables to the project models/ dir.

    Returns:
        tuple: (model_dir, gguf_dir) as Path objects.
    """
    if project_root is None:
        project_root = get_project_root()
    model_dir = project_root / "models"
    gguf_dir = model_dir / "gguf"
    model_dir.mkdir(parents=True, exist_ok=True)
    gguf_dir.mkdir(parents=True, exist_ok=True)

    os.environ["MODEL_CACHE_DIR"] = str(model_dir)
    os.environ["MARKER_MODEL_DIR"] = str(model_dir)
    os.environ["HF_HOME"] = str(model_dir / "hf_home")
    os.environ["SURYA_GGUF_LOCAL_MODEL_PATH"] = str(gguf_dir / "surya-2.gguf")
    os.environ["SURYA_GGUF_LOCAL_MMPROJ_PATH"] = str(gguf_dir / "surya-2-mmproj.gguf")
    # Prefer the HF mirror for users in CN networks
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    return model_dir, gguf_dir


class ModelItem:
    """Describes one model: source kind, remote source, local location."""

    def __init__(self, name, kind, source, local_path, required=True, extra_files=None):
        self.name = name            # short display name
        self.kind = kind            # 's3' | 'hf' | 'gguf'
        self.source = source        # e.g. s3://text_detection/2025_05_07 or HF repo id
        self.local_path = Path(local_path)
        self.required = required    # needed by the current default (balanced/GPU) mode
        self.extra_files = extra_files or []  # for gguf: additional files in the repo

    @property
    def status(self):
        """Local status: 'ready' | 'missing'."""
        if self.kind == 'gguf':
            ok = all((self.local_path / f).is_file() for f in [self.extra_files[0]] if f)
            ok = ok or self.local_path.is_file()
            return 'ready' if ok else 'missing'
        if self.kind == 's3':
            has_files = any(p.is_file() for p in self.local_path.rglob('*')) if self.local_path.exists() else False
            return 'ready' if has_files else 'missing'
        if self.kind == 'hf':
            snap = self._hf_snapshot_dir()
            complete = snap.exists() and any(snap.rglob('*'))
            return 'ready' if complete else 'missing'
        return 'unknown'

    def _hf_snapshot_dir(self):
        hub = Path(os.environ.get("HF_HOME", "")) / "hub"
        repo_dir = hub / f"models--{self.source.replace('/', '--')}" / "snapshots"
        if repo_dir.exists():
            snaps = [s for s in repo_dir.iterdir() if s.is_dir()]
            if snaps:
                return snaps[0]
        return repo_dir / "none"


def build_model_list(settings=None):
    """
    Build the model inventory from surya settings.

    Args:
        settings: surya settings object (imported after env setup).

    Returns:
        list[ModelItem]
    """
    from surya.settings import settings as s
    model_dir = Path(os.environ.get("MODEL_CACHE_DIR", get_project_root() / "models"))
    gguf_dir = model_dir / "gguf"

    items = [
        ModelItem(
            "gguf_vlm", "gguf", s.SURYA_GGUF_REPO, gguf_dir,
            required=True,
            extra_files=[s.SURYA_GGUF_MODEL_FILE, s.SURYA_GGUF_MMPROJ_FILE],
        ),
        ModelItem(
            "text_detection", "s3", s.DETECTOR_MODEL_CHECKPOINT,
            model_dir / "text_detection" / s.DETECTOR_MODEL_CHECKPOINT.replace("s3://", "").split("/", 1)[1],
        ),
        ModelItem(
            "ocr_error_detection", "s3", s.OCR_ERROR_MODEL_CHECKPOINT,
            model_dir / "ocr_error_detection" / s.OCR_ERROR_MODEL_CHECKPOINT.replace("s3://", "").split("/", 1)[1],
        ),
        ModelItem(
            "fast_layout", "hf", s.FAST_LAYOUT_MODEL_CHECKPOINT.replace("hf://", ""),
            model_dir / "hf_home", required=False,
        ),
        ModelItem(
            "vlm_torch", "hf", s.SURYA_MODEL_CHECKPOINT,
            model_dir / "hf_home", required=False,
        ),
    ]
    return items


def remote_version(item):
    """
    Query the remote latest version for an item.

    Returns:
        str: version string ('n/a' when unavailable / offline).
    """
    try:
        if item.kind == 'gguf' or item.kind == 'hf':
            from huggingface_hub import HfApi
            api = HfApi(endpoint=os.environ.get("HF_ENDPOINT"))
            commits = api.list_repo_commits(item.source)
            if commits:
                return commits[0].commit_id[:12]
            return "n/a"
        if item.kind == 's3':
            # The checkpoint path itself carries the version (date tag)
            return item.source.replace("s3://", "")
    except Exception as e:
        return f"n/a ({e.__class__.__name__})"


def local_version(item):
    """Return the local version tag for an item."""
    if item.kind == 's3':
        return item.source.replace("s3://", "").split("/", 1)[1] if item.status == 'ready' else "-"
    if item.kind == 'gguf':
        meta = item.local_path / "surya-2.gguf.metadata.json"
        if meta.is_file():
            try:
                return json.loads(meta.read_text(encoding="utf-8")).get("commit", "local")
            except Exception:
                return "local"
        return "local"
    if item.kind == 'hf':
        snap = item._hf_snapshot_dir()
        return snap.name[:12] if snap.name != "none" and item.status == 'ready' else "-"
    return "-"


def download_model(item, force=False):
    """
    Download / update one model into the project models directory.

    Returns:
        bool: True on success.
    """
    try:
        if item.kind == 's3':
            from surya.common.s3 import download_directory
            checkpoint = item.source.replace("s3://", "")
            print(f"{Colors.BLUE}  Downloading s3 model {checkpoint} -> {item.local_path}{Colors.RESET}")
            item.local_path.parent.mkdir(parents=True, exist_ok=True)
            download_directory(checkpoint, str(item.local_path))
            return True

        if item.kind == 'gguf':
            from huggingface_hub import hf_hub_download
            item.local_path.mkdir(parents=True, exist_ok=True)
            commits = None
            try:
                from huggingface_hub import HfApi
                commits = HfApi(endpoint=os.environ.get("HF_ENDPOINT")).list_repo_commits(item.source)
            except Exception:
                pass
            for fname in item.extra_files:
                target = item.local_path / fname
                if force or not target.is_file():
                    print(f"{Colors.BLUE}  Downloading {fname} from {item.source} ...{Colors.RESET}")
                    hf_hub_download(
                        item.source, fname, local_dir=str(item.local_path),
                        force_download=force,
                    )
            if commits:
                (item.local_path / "surya-2.gguf.metadata.json").write_text(
                    json.dumps({"commit": commits[0].commit_id[:12], "repo": item.source}),
                    encoding="utf-8",
                )
            return True

        if item.kind == 'hf':
            from huggingface_hub import snapshot_download
            print(f"{Colors.BLUE}  Downloading HF model {item.source} ...{Colors.RESET}")
            snapshot_download(item.source, local_dir_use_symlinks=False)
            return True

    except Exception as e:
        print(f"{Colors.RED}  Failed to download {item.name}: {e}{Colors.RESET}")
        return False
    return False


def check_models(check_remote=True):
    """
    Inspect every model and return (items, report_lines).

    Args:
        check_remote: also query remote latest versions.
    """
    items = build_model_list()
    rows = []
    for it in items:
        st = it.status
        lv = local_version(it)
        rv = remote_version(it) if check_remote else "-"
        rows.append((it, st, lv, rv))
    return items, rows


def ensure_models(auto_download=True, check_remote=False, force=False):
    """
    Ensure all required models are present locally; download when missing.

    Args:
        auto_download: download missing models (default True).
        check_remote: query remote versions before deciding.
        force: re-download even when present.

    Returns:
        bool: True when all required models are ready.
    """
    setup_model_env()
    items, rows = check_models(check_remote=check_remote)
    print(f"\n{Colors.CYAN}Model Inventory (dir: {os.environ['MODEL_CACHE_DIR']}){Colors.RESET}")
    print("-" * 78)
    header = f"{'Model':<22}{'Status':<10}{'Local version':<24}{'Remote latest'}"
    print(header)
    print("-" * 78)

    all_ready = True
    for it, st, lv, rv in rows:
        marker = ""
        if st != 'ready':
            marker = Colors.YELLOW if it.required else Colors.BLUE
            if it.required:
                all_ready = False
            print(f"{it.name:<22}{Colors.YELLOW if it.required else Colors.BLUE}{st:<10}{Colors.RESET}{lv:<24}{rv}")
            if auto_download and it.required:
                print(f"  -> downloading...")
                ok = download_model(it, force=force)
                print(f"  {'OK' if ok else 'FAILED'}\n")
        else:
            print(f"{it.name:<22}{Colors.GREEN}{st:<10}{Colors.RESET}{lv:<24}{rv}")

    print("-" * 78)
    return all_ready


def prune_stale():
    """
    Remove legacy model directories that are no longer referenced by
    current surya settings (e.g. 1.x-era text_recognition / table_recognition).
    Only removes directories inside the project models/ folder.
    """
    model_dir = Path(os.environ.get("MODEL_CACHE_DIR", get_project_root() / "models"))
    current = set()
    for it in build_model_list():
        if it.kind == 's3':
            rel = it.source.replace("s3://", "").split("/", 1)[0]
            current.add(rel)
    legacy_names = ['text_recognition', 'table_recognition']
    removed = []
    for name in legacy_names:
        p = model_dir / name
        if p.exists():
            print(f"{Colors.YELLOW}Removing legacy model dir: {p}{Colors.RESET}")
            import shutil
            shutil.rmtree(p, ignore_errors=True)
            removed.append(name)
    return removed


def main():
    parser = argparse.ArgumentParser(description="Manage marker/surya models (dir + updates)")
    parser.add_argument("--check", action="store_true", help="report only, no download")
    parser.add_argument("--update", action="store_true", help="force re-check remote and update")
    parser.add_argument("--prune", action="store_true", help="remove stale legacy model dirs")
    args = parser.parse_args()

    setup_model_env()

    if args.prune:
        removed = prune_stale()
        print(f"Pruned: {removed if removed else 'nothing'}")
        return

    auto_download = not args.check
    ok = ensure_models(auto_download=auto_download, check_remote=True, force=args.update)

    if not ok:
        print(f"\n{Colors.RED}Some required models are missing and could not be downloaded.{Colors.RESET}")
        print("Check network / HF mirror and retry.")
        raise SystemExit(1)
    print(f"\n{Colors.GREEN}All required models are ready.{Colors.RESET}")


if __name__ == "__main__":
    main()

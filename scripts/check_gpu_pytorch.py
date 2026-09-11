#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: check_gpu_pytorch.py

Purpose:
    This script checks GPU availability and verifies PyTorch configuration
    to ensure the system is ready for GPU-accelerated processing.

Usage:
    python scripts/check_gpu_pytorch.py

Virtual Environment:
    This script should be run within the project's virtual environment.
    
    Virtual environment location: ./venv
    
    To activate the virtual environment (Windows):
    venv\\Scripts\\activate

Dependencies:
    - Python 3.10.11+
    - pytorch

Author:
    MiouCat Workshop
    Date: 2026-02-14

License:
    MIT License
"""

import torch

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
        """Colorize text for terminal output"""
        return f"{color}{text}{Colors.RESET}"

def main():
    """Main function to check GPU and PyTorch status."""
    print(f"{Colors.CYAN}Checking PyTorch and GPU configuration...{Colors.RESET}")
    print()
    
    # Check PyTorch version
    print(f"{Colors.BLUE}PyTorch version:{Colors.RESET} {torch.__version__}")
    
    # Check CUDA availability
    cuda_available = torch.cuda.is_available()
    status = Colors.GREEN if cuda_available else Colors.RED
    print(f"{Colors.BLUE}CUDA available:{Colors.RESET} {status}{cuda_available}{Colors.RESET}")
    
    # Check CUDA version
    cuda_version = torch.version.cuda if cuda_available else 'N/A'
    print(f"{Colors.BLUE}CUDA version:{Colors.RESET} {cuda_version}")
    
    # Check CUDA device count
    device_count = torch.cuda.device_count()
    print(f"{Colors.BLUE}CUDA devices count:{Colors.RESET} {device_count}")
    print()
    
    # Check device details if CUDA is available
    if cuda_available:
        print(f"{Colors.BLUE}Current device:{Colors.RESET} {torch.cuda.current_device()}")
        print(f"{Colors.BLUE}Device name:{Colors.RESET} {torch.cuda.get_device_name(0)}")
    else:
        print(f"{Colors.YELLOW}No CUDA GPU available. Using CPU.{Colors.RESET}")
    print()
    
    # Test PyTorch basic functionality
    try:
        # Create a simple tensor to test PyTorch
        test_tensor = torch.tensor([1.0, 2.0, 3.0])
        print(f"{Colors.GREEN}PyTorch basic functionality test passed.{Colors.RESET}")
        
        # Test GPU functionality if available
        if cuda_available:
            test_tensor_gpu = test_tensor.to('cuda')
            print(f"{Colors.GREEN}GPU functionality test passed.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}PyTorch test failed: {e}{Colors.RESET}")
    print()
    
    # Add conclusion and recommendation
    print(f"{Colors.CYAN}=== Conclusion ==={Colors.RESET}")
    if cuda_available:
        print(f"{Colors.GREEN}Recommendation: Use GPU-accelerated scripts for better performance.{Colors.RESET}")
        print(f"{Colors.GREEN}Your system is ready for GPU-based processing.{Colors.RESET}")
    else:
        print(f"{Colors.YELLOW}Recommendation: Use CPU-only scripts as no GPU is available.{Colors.YELLOW}")
        print(f"{Colors.YELLOW}Your system will use CPU for all processing tasks.{Colors.YELLOW}")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: check_image_sizes.py

Purpose:
    This script checks the dimensions of image files in a specified directory,
    particularly focusing on _page_* files that are typically intermediate
    products from PDF conversion processes.

Usage:
    python scripts/check_image_sizes.py <image_directory>

    Example:
    python scripts/check_image_sizes.py "path/to/images"

Virtual Environment:
    This script should be run within the project's virtual environment.
    
    Virtual environment location: ./venv
    
    To activate the virtual environment (Windows):
    venv\Scripts\activate

Dependencies:
    - Python 3.10.11+
    - Pillow (PIL)

Author:
    MiouCat Workshop
    Date: 2026-02-27

License:
    MIT License
"""

import os
import sys
from PIL import Image

# Terminal color codes
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

# Check command line arguments
if len(sys.argv) != 2:
    print(f"{Colors.RED}Usage: python check_image_sizes.py <image_directory>{Colors.RESET}")
    sys.exit(1)

# Get image directory path
image_dir = sys.argv[1]

# Check if directory exists
if not os.path.exists(image_dir):
    print(f"{Colors.RED}Error: Directory '{image_dir}' does not exist{Colors.RESET}")
    sys.exit(1)

# Check if path is a directory
if not os.path.isdir(image_dir):
    print(f"{Colors.RED}Error: '{image_dir}' is not a directory{Colors.RESET}")
    sys.exit(1)

print(f"{Colors.CYAN}Checking image sizes in directory:{Colors.RESET}")
print(f"{Colors.BLUE}{image_dir}{Colors.RESET}")
print(f"{Colors.YELLOW}{'-' * 80}{Colors.RESET}")

# Initialize counters
processed_files = 0
error_files = 0

# Process images
for file in os.listdir(image_dir):
    # Only process _page_* image files
    if file.startswith('_page_') and file.endswith('.jpeg'):
        file_path = os.path.join(image_dir, file)
        try:
            # Open image and get dimensions
            img = Image.open(file_path)
            width = img.width
            height = img.height
            aspect_ratio = width / height
            
            # Determine aspect ratio category
            if aspect_ratio > 10:
                aspect_category = f"{Colors.RED}Very wide{Colors.RESET}"
            elif aspect_ratio > 5:
                aspect_category = f"{Colors.YELLOW}Wide{Colors.RESET}"
            elif aspect_ratio > 2:
                aspect_category = f"{Colors.GREEN}Moderate{Colors.RESET}"
            else:
                aspect_category = f"{Colors.CYAN}Square{Colors.RESET}"
            
            # Print results
            print(f"{file}: Width={width}, Height={height}, Aspect={aspect_ratio:.2f} ({aspect_category})")
            
            # Close image
            img.close()
            processed_files += 1
        except Exception as e:
            print(f"{Colors.RED}{file}: Error - {e}{Colors.RESET}")
            error_files += 1

print(f"{Colors.YELLOW}{'-' * 80}{Colors.RESET}")
print(f"{Colors.GREEN}Processing completed:{Colors.RESET}")
print(f"- Processed files: {processed_files}")
print(f"- Error files: {error_files}")
print(f"- Total _page_* files: {processed_files + error_files}")
print(f"{Colors.CYAN}Done.{Colors.RESET}")

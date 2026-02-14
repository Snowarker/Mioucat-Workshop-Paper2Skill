#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: analyze_pdf_images.py

Purpose:
    This script analyzes PDF files to identify image types and properties, including
    format, dimensions, size, and whether images are raster or vector type.

Usage:
    python scripts/analyze_pdf_images.py

    The script automatically analyzes the test PDF file located in the project structure.

Virtual Environment:
    This script should be run within the project's virtual environment.
    
    Virtual environment location: ./venv
    
    To activate the virtual environment (Windows):
    venv\\Scripts\\activate

Dependencies:
    - Python 3.10.11+
    - PyMuPDF (fitz)

Author:
    MiouCat Workshop
    Date: 2026-02-14

License:
    MIT License
"""

import fitz
import os
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
        """Colorize text for terminal output"""
        return f"{color}{text}{Colors.RESET}"

def analyze_pdf_images(pdf_path):
    """
    Analyze PDF file to identify image types and properties.
    
    Args:
        pdf_path (str): Path to the PDF file
    """
    print(f"{Colors.CYAN}Analyzing PDF:{Colors.RESET} {pdf_path}")
    print("=" * 60)
    
    try:
        # Open PDF file
        doc = fitz.open(pdf_path)
        print(f"{Colors.BLUE}PDF contains {doc.page_count} pages{Colors.RESET}")
        print()
        
        image_count = 0
        
        # Iterate through pages
        for page_num in range(len(doc)):
            page = doc[page_num]
            images = page.get_images(full=True)
            
            if images:
                print(f"{Colors.BLUE}Page {page_num + 1}: {len(images)} images{Colors.RESET}")
                
                # Analyze each image
                for img_index, img in enumerate(images):
                    image_count += 1
                    xref = img[0]
                    
                    # Get image info
                    img_info = doc.extract_image(xref)
                    img_data = img_info.get('image', b'')
                    img_ext = img_info.get('ext', 'unknown')
                    img_width = img_info.get('width', 0)
                    img_height = img_info.get('height', 0)
                    img_size = len(img_data) / 1024  # KB
                    
                    # Get image details from the PDF
                    img_dict = doc.xref_object(xref)
                    
                    print(f"  {Colors.GREEN}Image {img_index + 1}:{Colors.RESET}")
                    print(f"    Format: {img_ext}")
                    print(f"    Dimensions: {img_width}x{img_height}")
                    print(f"    Size: {img_size:.2f} KB")
                    print(f"    XREF: {xref}")
                    
                    # Check if it's a vector image (PDF form XObject)
                    if 'Form' in img_dict:
                        print("    Type: Vector (Form XObject)")
                    else:
                        print("    Type: Raster")
                    
                    print()
        
        print("=" * 60)
        print(f"{Colors.GREEN}Total images found: {image_count}{Colors.RESET}")
        print("=" * 60)
        
        doc.close()
        
    except Exception as e:
        print(f"{Colors.RED}Error analyzing PDF: {str(e)}{Colors.RESET}")

def main():
    """
    Main function to analyze PDF images in all subdirectories.
    """
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    # Path to the input directory
    input_dir = project_root / "pdf" / "input"
    
    if not input_dir.exists():
        print(f"{Colors.RED}Input directory not found: {input_dir}{Colors.RESET}")
        return
    
    print(f"{Colors.CYAN}Starting PDF image analysis...{Colors.RESET}")
    print(f"{Colors.BLUE}Input directory:{Colors.RESET} {input_dir}")
    print()
    
    # Collect all PDF files in subdirectories
    pdf_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = Path(root) / file
                pdf_files.append(pdf_path)
    
    if not pdf_files:
        print(f"{Colors.YELLOW}No PDF files found in input directory.{Colors.RESET}")
        return
    
    print(f"{Colors.BLUE}Found {len(pdf_files)} PDF files to analyze:{Colors.RESET}")
    for pdf_path in pdf_files:
        relative_path = pdf_path.relative_to(input_dir)
        print(f"  • {relative_path}")
    print()
    
    # Analyze each PDF file
    total_images = 0
    for pdf_path in pdf_files:
        print(f"{Colors.CYAN}\nAnalyzing: {pdf_path.relative_to(input_dir)}{Colors.RESET}")
        print("-" * 80)
        
        # Count images in this PDF
        try:
            doc = fitz.open(pdf_path)
            doc_images = 0
            for page_num in range(len(doc)):
                page = doc[page_num]
                images = page.get_images(full=True)
                doc_images += len(images)
            doc.close()
            total_images += doc_images
            
            print(f"{Colors.GREEN}PDF contains {doc_images} images{Colors.RESET}")
        except Exception as e:
            print(f"{Colors.RED}Error analyzing {pdf_path}: {str(e)}{Colors.RESET}")
        
        # Call the existing analyze function
        analyze_pdf_images(str(pdf_path))
    
    # Final summary
    print(f"{Colors.CYAN}\n=== Final Summary ==={Colors.RESET}")
    print(f"{Colors.BLUE}Total PDF files analyzed:{Colors.RESET} {len(pdf_files)}")
    print(f"{Colors.GREEN}Total images found:{Colors.RESET} {total_images}")
    print(f"{Colors.CYAN}====================={Colors.RESET}")

if __name__ == "__main__":
    main()
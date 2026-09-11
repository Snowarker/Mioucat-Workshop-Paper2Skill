#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: process_pdf.py

Purpose:
    This script processes PDF files to extract structured content for scientific publication.
    It uses Marker's default parameters to generate Markdown files and image folders
    from PDF documents, handling special characters in filenames automatically.
    Adapted for marker-pdf 2.x API.

Usage:
    python scripts/process_pdf.py

    The script automatically detects the input and output directories based on its relative position.
    On startup it calls manage_models.ensure_models() to verify/download required
    models into the project models/ directory (see manage_models.py for the
    standalone model directory & update management).

Virtual Environment:
    This script should be run within the project's virtual environment.
    
    Virtual environment location: ./venv
    
    To activate the virtual environment (Windows):
    venv\\Scripts\\activate

Dependencies:
    - Python 3.10.11+
    - marker-pdf >= 2.0
    - pytorch (GPU build recommended)
    - numpy
    - fitz (PyMuPDF)
    - pillow

Author:
    MiouCat Workshop
    Date: 2026-09-11 (updated for marker-pdf 2.x)

License:
    MIT License
"""

import os
import re
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
        """Colorize text for terminal output"""
        return f"{color}{text}{Colors.RESET}"

# Model path & version management lives in manage_models.py (independent script).
# It must set environment variables BEFORE importing Marker/Surya.
from manage_models import setup_model_env, ensure_models, get_project_root

model_dir, gguf_dir = setup_model_env()
print(f"Model directory: {model_dir}")
print(f"MODEL_CACHE_DIR: {os.environ.get('MODEL_CACHE_DIR', 'NOT SET')}")
print(f"HF_HOME: {os.environ.get('HF_HOME', 'NOT SET')}")
print(f"SURYA_GGUF_LOCAL_MODEL_PATH: {os.environ.get('SURYA_GGUF_LOCAL_MODEL_PATH', 'NOT SET')}")

# Now import Marker modules
from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

# Import Surya settings to verify the actual model directory
try:
    from surya.settings import settings
    print(f"\nSurya settings model cache dir: {settings.MODEL_CACHE_DIR}")
except Exception as e:
    print(f"Error importing Surya settings: {str(e)}")


def sanitize_filename(filename):
    """
    Sanitize filename by replacing special characters with underscores.
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Sanitized filename
    """
    sanitized = re.sub(r'[^a-zA-Z0-9._-]', '_', filename)
    sanitized = re.sub(r'_+', '_', sanitized)
    sanitized = sanitized.strip('_')
    return sanitized


def count_pdf_images(pdf_path):
    """
    Count the actual number of images in a PDF file using PyMuPDF.
    
    Args:
        pdf_path (Path): Path to the PDF file
        
    Returns:
        int: Number of images found in the PDF
    """
    try:
        import fitz
        doc = fitz.open(str(pdf_path))
        total_images = 0
        for page_num in range(len(doc)):
            page = doc[page_num]
            images = page.get_images(full=True)
            total_images += len(images)
        doc.close()
        return total_images
    except Exception as e:
        print(f"Error counting PDF images: {str(e)}")
        return 0

def save_output_files(rendered, output_dir, fname_base):
    """
    Save markdown and images using marker 2.x save_output helper.
    
    Args:
        rendered: marker rendered output object
        output_dir (Path): Directory to save files
        fname_base (str): Base name for output files
    """
    from marker.output import save_output
    output_dir.mkdir(parents=True, exist_ok=True)
    save_output(rendered, str(output_dir), fname_base)
    return fname_base

def process_pdf_file(pdf_path, output_dir, model_dir):
    """
    Process a single PDF file using Marker's default parameters.
    Only processes parts that haven't been completed yet.
    
    Args:
        pdf_path (Path): Path to the PDF file
        output_dir (Path): Directory to save output files
        model_dir (Path): Directory to store model files
    """
    import multiprocessing
    
    print(f"{Colors.BLUE}Processing PDF:{Colors.RESET} {pdf_path}")
    print(f"{Colors.BLUE}Using model directory:{Colors.RESET} {model_dir}")
    
    # Generate sanitized filename
    pdf_filename = pdf_path.stem
    sanitized_filename = sanitize_filename(pdf_filename)
    markdown_path = output_dir / f"{sanitized_filename}.md"
    images_dir = output_dir / f"{sanitized_filename}_images"
    
    # Calculate CPU cores limit (half of max cores)
    max_cores = multiprocessing.cpu_count()
    cores_limit = max(1, max_cores // 2)
    print(f"{Colors.BLUE}System CPU cores:{Colors.RESET} {max_cores}")
    print(f"{Colors.BLUE}Using CPU cores limit:{Colors.RESET} {cores_limit}")
    
    try:
        # Create output directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)
        model_dir.mkdir(parents=True, exist_ok=True)
        
        # Count actual images in PDF
        expected_images = count_pdf_images(pdf_path)
        print(f"{Colors.BLUE}Expected images in PDF:{Colors.RESET} {expected_images}")
        
        # Check if we need to process the PDF
        need_full_processing = not markdown_path.exists()
        
        # Check if images are valid
        has_valid_images = False
        valid_image_count = 0
        if images_dir.exists():
            for img_file in images_dir.iterdir():
                if img_file.is_file() and img_file.stat().st_size > 0:
                    valid_image_count += 1
            # Check if we have at least as many valid images as expected
            has_valid_images = valid_image_count >= expected_images if expected_images > 0 else False
        
        need_image_extraction = not has_valid_images
        
        if not need_full_processing and not need_image_extraction:
            print(f"{Colors.GREEN}All processing for {pdf_path} is complete. Skipping.{Colors.RESET}")
            print(f"{Colors.BLUE}Found {valid_image_count} valid images (expected {expected_images}){Colors.RESET}")
            return
        elif not need_full_processing and need_image_extraction:
            print(f"{Colors.YELLOW}Need to extract images for {pdf_path}{Colors.RESET}")
            print(f"{Colors.BLUE}Found {valid_image_count} valid images, but expected {expected_images}{Colors.RESET}")
        
        # Initialize Marker converter (marker 2.x API)
        converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config={
                "mode": "balanced",  # GPU 默认模式；CPU 上可改 "fast"
            }
        )
        
        # Convert PDF file
        print(f"{Colors.YELLOW}Converting PDF file...{Colors.RESET}")
        rendered = converter(str(pdf_path))
        
        # Save markdown and images using marker's save_output helper
        print(f"{Colors.YELLOW}Saving markdown and images...{Colors.RESET}")
        markdown_text, ext, images = text_from_rendered(rendered)
        
        if not markdown_path.exists():
            save_output_files(rendered, output_dir, sanitized_filename)
            print(f"{Colors.GREEN}Saved Markdown:{Colors.RESET} {markdown_path}")
        else:
            print(f"{Colors.BLUE}Markdown file already exists:{Colors.RESET} {markdown_path}")
            # Still save images if needed
            if need_image_extraction and images:
                save_output_files(rendered, output_dir, sanitized_filename)
                print(f"{Colors.GREEN}Saved images to:{Colors.RESET} {images_dir}")
        
        # Verify saved images
        saved_count = 0
        if images_dir.exists():
            saved_count = sum(1 for f in images_dir.iterdir() if f.is_file() and f.stat().st_size > 0)
        print(f"{Colors.BLUE}Saved images count:{Colors.RESET} {saved_count}")
        if saved_count < expected_images:
            print(f"{Colors.YELLOW}Note: extracted {saved_count} images, expected {expected_images} (marker 2.x extracts referenced images only){Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error processing {pdf_path}: {str(e)}{Colors.RESET}")
        import traceback
        traceback.print_exc()


def check_model_availability():
    """
    Check models via manage_models.py and download any missing required ones.
    Returns True when all required models are ready.
    """
    print("\nChecking model availability...")
    try:
        return ensure_models(auto_download=True, check_remote=False)
    except Exception as e:
        print(f"Error checking model availability: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def process_all_pdfs():
    """
    Process all PDF files in the input directory structure.
    Only processes files that haven't been fully processed yet.
    """
    # Get project root directory
    project_root = get_project_root()
    print(f"Project root: {project_root}")
    
    # Define input, output, and model directories
    pdf_dir = project_root / "pdf"
    input_dir = pdf_dir / "input"
    output_dir = pdf_dir / "output"
    model_dir = project_root / "models"
    
    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")
    print(f"Model directory: {model_dir}")
    print(f"Model directory exists: {model_dir.exists()}")
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory created successfully: {output_dir}")
    
    # Model directory is already created at script startup
    
    # First check if models are available
    if not check_model_availability():
        print("\nModel check failed. Please check your internet connection and try again.")
        return
    
    # Collect input structure information
    print(f"\n{Colors.CYAN}Input Structure Analysis:{Colors.RESET}")
    print("-" * 50)
    
    total_dirs = 0
    total_pdfs = 0
    dir_pdf_map = {}
    
    # First pass: collect directory and PDF information
    for root, dirs, files in os.walk(input_dir):
        # Calculate relative path from input directory
        relative_path = os.path.relpath(root, input_dir)
        
        # Skip the input directory itself
        if relative_path == '.':
            continue
        
        total_dirs += 1
        pdf_files = [file for file in files if file.lower().endswith('.pdf')]
        total_pdfs += len(pdf_files)
        dir_pdf_map[relative_path] = pdf_files
    
    # Print input structure summary
    print(f"{Colors.BLUE}Total directories:{Colors.RESET} {total_dirs}")
    print(f"{Colors.BLUE}Total PDF files:{Colors.RESET} {total_pdfs}")
    
    if dir_pdf_map:
        print(f"\n{Colors.BLUE}Directories:{Colors.RESET}")
        for dir_path, pdf_files in dir_pdf_map.items():
            print(f"  • {dir_path} ({len(pdf_files)} PDFs)")
            if pdf_files:
                for pdf_file in pdf_files:
                    print(f"    - {pdf_file}")
    
    # Second pass: process files
    print(f"\n{Colors.CYAN}Starting PDF Processing...{Colors.RESET}")
    print("-" * 50)
    
    processed_count = 0
    skipped_count = 0
    
    for root, dirs, files in os.walk(input_dir):
        # Calculate relative path from input directory
        relative_path = os.path.relpath(root, input_dir)
        
        # Skip the input directory itself
        if relative_path == '.':
            continue
        
        # Create corresponding output directory
        current_output_dir = output_dir / relative_path
        current_output_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"\n{Colors.BLUE}Processing directory:{Colors.RESET} {relative_path}")
        
        # Process all PDF files in the current directory
        dir_processed = 0
        dir_skipped = 0
        
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = Path(root) / file
                # Create subdirectory for this PDF file
                pdf_output_dir = current_output_dir / sanitize_filename(Path(file).stem)
                
                # Check if this PDF has already been processed
                md_file = pdf_output_dir / f"{sanitize_filename(Path(file).stem)}.md"
                images_dir = pdf_output_dir / f"{sanitize_filename(Path(file).stem)}_images"
                
                # Check if processing is complete
                if md_file.exists():
                    # Check if images directory exists and has valid files
                    has_valid_images = False
                    valid_image_count = 0
                    if images_dir.exists():
                        for img_file in images_dir.iterdir():
                            if img_file.is_file() and img_file.stat().st_size > 0:
                                valid_image_count += 1
                        has_valid_images = valid_image_count > 0
                    
                    if has_valid_images:
                        print(f"  {Colors.GREEN}✓{Colors.RESET} {file} - already processed (images: {valid_image_count})")
                        dir_skipped += 1
                        skipped_count += 1
                        continue
                    else:
                        print(f"  {Colors.YELLOW}→{Colors.RESET} {file} - extracting images")
                else:
                    print(f"  {Colors.YELLOW}→{Colors.RESET} {file} - processing")
                
                # Count actual images in PDF before processing
                expected_images = count_pdf_images(pdf_path)
                print(f"    {Colors.BLUE}Images detected:{Colors.RESET} {expected_images}")
                
                # Process the PDF file
                process_pdf_file(pdf_path, pdf_output_dir, model_dir)
                dir_processed += 1
                processed_count += 1
        
        if dir_processed > 0 or dir_skipped > 0:
            print(f"  {Colors.BLUE}Summary:{Colors.RESET} {dir_processed} newly processed, {dir_skipped} already completed")
    
    # Final summary
    print(f"\n{Colors.CYAN}Processing Summary:{Colors.RESET}")
    print("-" * 50)
    print(f"{Colors.BLUE}Directories processed:{Colors.RESET} {total_dirs}")
    print(f"{Colors.BLUE}Total PDF files:{Colors.RESET} {total_pdfs}")
    print(f"{Colors.GREEN}Successfully processed:{Colors.RESET} {processed_count + skipped_count}")
    print(f"{Colors.GREEN}Newly processed:{Colors.RESET} {processed_count}")
    print(f"{Colors.YELLOW}Already completed (skipped):{Colors.RESET} {skipped_count}")
    if total_pdfs > 0:
        success_rate = (processed_count + skipped_count) / total_pdfs * 100
        print(f"{Colors.BLUE}Processing rate:{Colors.RESET} {(processed_count + skipped_count)}/{total_pdfs} ({success_rate:.1f}%)")
    print(f"\n{Colors.GREEN}Processing completed!{Colors.RESET}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process PDF files using Marker")
    args = parser.parse_args()
    
    print("Starting PDF processing...")
    process_all_pdfs()
    print("\nPDF processing completed!")

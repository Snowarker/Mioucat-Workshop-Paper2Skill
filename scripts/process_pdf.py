#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Name: process_pdf.py

Purpose:
    This script processes PDF files to extract structured content for scientific publication.
    It uses Marker's default parameters to generate Markdown files and image folders
    from PDF documents, handling special characters in filenames automatically.

Usage:
    python scripts/process_pdf.py

    The script automatically detects the input and output directories based on its relative position.

Virtual Environment:
    This script should be run within the project's virtual environment.
    
    Virtual environment location: ./venv
    
    To activate the virtual environment (Windows):
    venv\\Scripts\\activate

Dependencies:
    - Python 3.10.11+
    - marker-pdf
    - pytorch
    - numpy
    - pandas
    - fitz (PyMuPDF)
    - pillow
    - base64

Author:
    MiouCat Workshop
    Date: 2026-02-14

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

# Set model directory environment variables BEFORE importing Marker/Surya
# This ensures the variables are set before Surya's settings are initialized

def get_project_root():
    """
    Get the project root directory based on the script's location.
    
    Returns:
        Path: Project root directory
    """
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    return project_root

# Calculate project root and model directory early
project_root = get_project_root()
model_dir = project_root / "models"

# Create model directory if it doesn't exist
print(f"Creating model directory: {model_dir}")
try:
    model_dir.mkdir(parents=True, exist_ok=True)
    print(f"Model directory created successfully: {model_dir}")
except Exception as e:
    print(f"Error creating model directory: {str(e)}")

# Set environment variables for model directory
print(f"Setting model directory environment variables to: {model_dir}")
os.environ["MODEL_CACHE_DIR"] = str(model_dir)
os.environ["MARKER_MODEL_DIR"] = str(model_dir)
print(f"MODEL_CACHE_DIR: {os.environ.get('MODEL_CACHE_DIR', 'NOT SET')}")
print(f"MARKER_MODEL_DIR: {os.environ.get('MARKER_MODEL_DIR', 'NOT SET')}")

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
        
        # Initialize Marker converter with CPU limit and image extraction settings
        converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config={
                "max_workers": cores_limit,
                "batch_size": min(4, cores_limit),
                "extract_images": need_image_extraction,
                "image_extraction_mode": "highres"
            }
        )
        
        # Convert PDF file
        print(f"{Colors.YELLOW}Converting PDF file...{Colors.RESET}")
        rendered = converter(str(pdf_path))
        
        # Extract text and images
        print(f"{Colors.YELLOW}Extracting text and images...{Colors.RESET}")
        markdown_text, metadata, images = text_from_rendered(rendered)
        
        # Save Markdown file if it doesn't exist
        if not markdown_path.exists():
            with open(markdown_path, 'w', encoding='utf-8') as f:
                f.write(markdown_text)
            print(f"{Colors.GREEN}Saved Markdown:{Colors.RESET} {markdown_path}")
        else:
            print(f"{Colors.BLUE}Markdown file already exists:{Colors.RESET} {markdown_path}")
        
        # Save images if needed
        if need_image_extraction and images:
            import io
            from PIL import Image
            
            images_dir.mkdir(exist_ok=True)
            
            saved_count = 0
            print(f"{Colors.BLUE}Found {len(images)} images to save...{Colors.RESET}")
            
            for img_name, img_data in images.items():
                img_path = images_dir / img_name
                try:
                    # Check if img_data is already bytes
                    if isinstance(img_data, bytes):
                        with open(img_path, 'wb') as f:
                            f.write(img_data)
                        saved_count += 1
                    # Check if img_data is a PIL Image object
                    elif isinstance(img_data, Image.Image):
                        # Convert Image object to bytes
                        img_buffer = io.BytesIO()
                        # Convert to RGB if needed
                        if img_data.mode != 'RGB':
                            img_data = img_data.convert('RGB')
                        img_data.save(img_buffer, format='JPEG')
                        img_bytes = img_buffer.getvalue()
                        with open(img_path, 'wb') as f:
                            f.write(img_bytes)
                        saved_count += 1
                    # Check if img_data is a base64 string
                    elif isinstance(img_data, str) and img_data.startswith('data:image/'):
                        # Extract base64 data
                        import base64
                        header, base64_data = img_data.split(',', 1)
                        img_bytes = base64.b64decode(base64_data)
                        with open(img_path, 'wb') as f:
                            f.write(img_bytes)
                        saved_count += 1
                    else:
                        print(f"{Colors.YELLOW}Unknown image data type for {img_name}: {type(img_data)}{Colors.RESET}")
                except Exception as e:
                    print(f"{Colors.RED}Error saving image {img_name}: {str(e)}{Colors.RESET}")
            
            print(f"{Colors.GREEN}Saved {saved_count}/{len(images)} images to:{Colors.RESET} {images_dir}")
        elif not need_image_extraction:
            print(f"{Colors.BLUE}Images already extracted. Skipping image processing.{Colors.RESET}")
        elif not images:
            print(f"{Colors.BLUE}No images found in PDF.{Colors.RESET}")
        
    except Exception as e:
        print(f"{Colors.RED}Error processing {pdf_path}: {str(e)}{Colors.RESET}")
        import traceback
        traceback.print_exc()


def check_model_availability():
    """
    Check if models are available, and download if necessary.
    This ensures models are ready before processing any PDFs.
    """
    print("\nChecking model availability...")
    
    try:
        # Import here to avoid circular imports
        from marker.models import create_model_dict
        from marker.converters.pdf import PdfConverter
        from surya.settings import settings
        
        # Print actual model directory being used
        print(f"Actual model directory being used by Surya: {settings.MODEL_CACHE_DIR}")
        print(f"Model directory exists: {os.path.exists(settings.MODEL_CACHE_DIR)}")
        
        # Create a minimal converter to trigger model download
        # This will check and download models if they don't exist
        converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config={"max_workers": 1, "batch_size": 1}
        )
        print("Models are available and ready!")
        return True
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

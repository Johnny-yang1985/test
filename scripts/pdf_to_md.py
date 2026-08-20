#!/usr/bin/env python3
"""
PDF to Markdown converter for LGES S32K3 BMS FBL User Manual
"""

import sys
import os
from pathlib import Path

def convert_pdf_to_md(pdf_path, output_dir):
    """Convert PDF to Markdown format"""
    try:
        # Try to import PyPDF2 or pymupdf
        try:
            import fitz  # PyMuPDF
            use_pymupdf = True
        except ImportError:
            try:
                import PyPDF2
                use_pymupdf = False
            except ImportError:
                print("Error: Neither PyMuPDF nor PyPDF2 is installed.")
                print("Please install one of them:")
                print("pip install PyMuPDF")
                print("or")
                print("pip install PyPDF2")
                return False
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract filename without extension
        pdf_name = Path(pdf_path).stem
        
        if use_pymupdf:
            # Use PyMuPDF
            doc = fitz.open(pdf_path)
            text_content = []
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()
                text_content.append(f"# 페이지 {page_num + 1}\n\n{text}\n\n---\n")
            
            doc.close()
        else:
            # Use PyPDF2
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text_content = []
                
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    text_content.append(f"# 페이지 {page_num + 1}\n\n{text}\n\n---\n")
        
        # Write to markdown file
        output_file = os.path.join(output_dir, f"{pdf_name}.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {pdf_name}\n\n")
            f.write("이 문서는 PDF에서 자동으로 변환된 문서입니다.\n\n")
            f.write("---\n\n")
            f.writelines(text_content)
        
        print(f"Successfully converted {pdf_path} to {output_file}")
        return True
        
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_md.py <pdf_path> <output_dir>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found")
        sys.exit(1)
    
    success = convert_pdf_to_md(pdf_path, output_dir)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()


















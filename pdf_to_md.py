import os
import fitz  # PyMuPDF
import re
try:
    from underthesea import word_tokenize
except ImportError:
    def word_tokenize(text):
        return text.split()

def clean_text(text):
    lines = text.split('\n')
    result = []
    
    contest_title = None
    problem_name = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # First line is contest title
        if i == 0 or (not contest_title and 'Contest' in line):
            contest_title = line
            result.append(f"# {line}\n")
            continue
            
        # Problem name (short uppercase)
        if not problem_name and len(line) < 15 and line.isupper():
            problem_name = line
            result.append(f"## {line}\n")
            continue
            
        # Section headers
        if line in ['Dữ liệu', 'Kết quả', 'Ví dụ']:
            result.append(f"\n## {line}\n")
            continue
            
        # Format bullets
        if line.startswith('•') or line.startswith('-'):
            line = re.sub(r'^[•-]\s*', '- ', line)
            
        # Fix math notation
        line = re.sub(r'F\s*\(\s*(\w+)\s*\)', r'F(\1)', line)
        line = re.sub(r'⊕', ' ⊕ ', line)
        
        # Fix Vietnamese spacing
        try:
            tokens = word_tokenize(line)
            line = ' '.join(tokens)
        except:
            pass
            
        line = re.sub(r'\s+', ' ', line)
        result.append(line)
    
    return '\n'.join(result)

def pdf_to_markdown(pdf_path, md_path):
    try:
        doc = fitz.open(pdf_path)
        all_text = []
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            if text.strip():
                all_text.append(text)
        
        doc.close()
        
        # Combine all pages
        full_text = '\n'.join(all_text)
        
        # Clean and format
        cleaned_text = clean_text(full_text)
        
        # Post-process for better structure
        cleaned_text = format_samples(cleaned_text)
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        
        return True
        
    except Exception as e:
        print(f"Error converting {pdf_path}: {e}")
        return False

def format_samples(text):
    # Find and format sample section
    sample_pattern = r'(\d+\s+\d+\s+\d+)\s*(\d+)\s*(\d+\s+\d+\s+\d+)\s*(\d+)\s*(\d+\s+\d+\s+\d+)\s*(\d+)'
    
    if re.search(sample_pattern, text):
        # Extract sample data
        match = re.search(sample_pattern, text)
        if match:
            samples = [
                (match.group(1), match.group(2)),
                (match.group(3), match.group(4)), 
                (match.group(5), match.group(6))
            ]
            
            sample_text = "\n**Ví dụ:**\n\n"
            for i, (inp, out) in enumerate(samples, 1):
                sample_text += f"*Ví dụ {i}:*\n```\n{inp}\n```\n```\n{out}\n```\n\n"
            
            # Replace the messy sample section
            text = re.sub(sample_pattern, sample_text, text)
    
    return text

def convert_all_pdfs():
    pdfs_dir = 'pdfs'
    mds_dir = 'mds'
    
    # Create markdown directory
    os.makedirs(mds_dir, exist_ok=True)
    
    if not os.path.exists(pdfs_dir):
        print(f"Directory {pdfs_dir} not found!")
        return
    
    pdf_files = [f for f in os.listdir(pdfs_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found!")
        return
    
    print(f"Converting {len(pdf_files)} PDF files to Markdown...")
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdfs_dir, pdf_file)
        md_file = pdf_file.replace('.pdf', '.md')
        md_path = os.path.join(mds_dir, md_file)
        
        print(f"Converting {pdf_file}...")
        
        if pdf_to_markdown(pdf_path, md_path):
            print(f"✓ Converted {pdf_file} -> {md_file}")
        else:
            print(f"✗ Failed to convert {pdf_file}")
    
    print("Conversion completed!")

if __name__ == "__main__":
    convert_all_pdfs()
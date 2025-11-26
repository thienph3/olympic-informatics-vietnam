import csv
import requests
import os
import time
from urllib.parse import urlparse

def download_pdfs():
    # Create pdfs directory if not exists
    os.makedirs('pdfs', exist_ok=True)
    
    with open('exercises_list.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['Type'] == 'Exercise' and row['PDF_Link']:
                pdf_url = row['PDF_Link']
                problem_name = row['Problem_Name']
                
                # Create filename
                filename = f"{problem_name}.pdf"
                filepath = os.path.join('pdfs', filename)
                
                # Skip if already downloaded
                if os.path.exists(filepath):
                    print(f"Skipped {filename} (already exists)")
                    continue
                
                try:
                    print(f"Downloading {filename}...")
                    
                    # Download with headers to avoid blocking
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    }
                    
                    response = requests.get(pdf_url, headers=headers, timeout=30)
                    
                    if response.status_code == 200:
                        with open(filepath, 'wb') as f:
                            f.write(response.content)
                        print(f"✓ Downloaded {filename}")
                    else:
                        print(f"✗ Failed {filename} (HTTP {response.status_code})")
                        
                except Exception as e:
                    print(f"✗ Error downloading {filename}: {e}")
                
                # Sleep to avoid being detected as crawler
                time.sleep(2)
    
    print("Download completed!")

if __name__ == "__main__":
    download_pdfs()
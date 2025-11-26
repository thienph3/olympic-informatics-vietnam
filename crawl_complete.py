#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import os

def append_to_csv(data):
    """Append data to CSV file"""
    file_exists = os.path.exists('vnoi_problems.csv')
    
    with open('vnoi_problems.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['contest_name', 'problem_name', 'problem_url', 'pdf_url', 'ggdrive_url'])
        writer.writerow(data)

def get_problem_links(problem_url):
    """Get PDF and Google Drive links from problem page"""
    try:
        response = requests.get(problem_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        pdf_url = ""
        ggdrive_url = ""
        
        # Find PDF links
        pdf_links = soup.find_all('a', href=re.compile(r'\.pdf$|vnoi-admin\.github\.io.*\.pdf'))
        if pdf_links:
            pdf_url = pdf_links[0]['href']
            if not pdf_url.startswith('http'):
                pdf_url = f"https://oj.vnoi.info{pdf_url}"
        
        # Find Google Drive links
        gdrive_links = soup.find_all('a', href=re.compile(r'drive\.google\.com'))
        if gdrive_links:
            ggdrive_url = gdrive_links[0]['href']
        
        return pdf_url, ggdrive_url
        
    except Exception as e:
        print(f"    Error getting problem links: {e}")
        return "", ""

def get_contest_problems(contest_url, contest_name):
    """Get all problems from a contest"""
    try:
        response = requests.get(contest_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        problem_links = soup.find_all('a', href=re.compile(r'/problem/'))
        problems = []
        
        for link in problem_links:
            problem_code = link['href'].split('/')[-1]
            problem_name = link.text.strip()
            
            if problem_code and len(problem_code) > 2:
                problems.append({
                    'code': problem_code,
                    'name': problem_name,
                    'url': f"https://oj.vnoi.info/problem/{problem_code}"
                })
        
        return problems
        
    except Exception as e:
        print(f"  Error getting contest problems: {e}")
        return []

def crawl_contests():
    """Main crawl function"""
    print("Starting VNOI complete crawl...")
    
    total_processed = 0
    
    # Crawl multiple pages
    for page in range(12, 31):  # First 30 pages
        try:
            url = f"https://oj.vnoi.info/contests/?page={page}"
            print(f"\nPage {page}...")
            
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            contest_links = soup.find_all('a', href=re.compile(r'/contest/'))
            
            for link in contest_links:
                contest_name = link.text.strip()
                contest_path = link['href']
                
                # Filter interesting contests
                if any(keyword in contest_name.lower() for keyword in [
                    'olympic', 'hsg', 'voi', 'tst', 'free contest', 'beginner', 'icpc'
                ]):
                    contest_url = f"https://oj.vnoi.info{contest_path}"
                    print(f"  Contest: {contest_name}")
                    
                    # Get problems from contest
                    problems = get_contest_problems(contest_url, contest_name)
                    
                    for problem in problems:
                        print(f"    Problem: {problem['code']}")
                        
                        # Get PDF and GDrive links
                        pdf_url, ggdrive_url = get_problem_links(problem['url'])
                        
                        # Debug: Stop if no links found
                        if not pdf_url and not ggdrive_url:
                            print(f"    ❌ NO LINKS FOUND - DEBUG URL: {problem['url']}")
                            return
                        
                        # Save to CSV
                        append_to_csv([
                            contest_name,
                            problem['name'],
                            problem['url'],
                            pdf_url,
                            ggdrive_url
                        ])
                        
                        total_processed += 1
                        print(f"    ✅ Saved ({total_processed} total)")
                        
                        time.sleep(0.1)  # Be nice to server
                    
                    time.sleep(0.2)
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"Error on page {page}: {e}")
    
    print(f"\nCrawl completed! Total problems processed: {total_processed}")
    print("Results saved to: vnoi_problems.csv")

if __name__ == "__main__":
    crawl_contests()
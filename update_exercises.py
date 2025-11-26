#!/usr/bin/env python3
import os
import csv
import re

def extract_info_from_md(filepath):
    """Extract category and difficulty from .md file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract category (Thể loại)
        category_match = re.search(r'\*\*Thể loại:\*\*\s*(.+)', content)
        category = category_match.group(1).strip() if category_match else "Unknown"
        
        # Extract difficulty (Độ khó)
        difficulty_match = re.search(r'\*\*Độ khó:\*\*\s*(\d+)', content)
        difficulty = int(difficulty_match.group(1)) if difficulty_match else 999
        
        return category, difficulty
    except:
        return "Unknown", 999

def update_exercises_csv():
    """Update exercises_list.csv with category and difficulty"""
    
    # Read existing CSV
    exercises = []
    with open('exercises_list.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        exercises = list(reader)
    
    # Update each exercise with category and difficulty
    for exercise in exercises:
        if exercise['Type'] == 'Exercise':
            problem_name = exercise['Problem_Name']
            md_path = f'mds/{problem_name}.md'
            
            if os.path.exists(md_path):
                category, difficulty = extract_info_from_md(md_path)
                exercise['Category'] = category
                exercise['Difficulty'] = difficulty
            else:
                exercise['Category'] = "Unknown"
                exercise['Difficulty'] = 999
        else:
            exercise['Category'] = ""
            exercise['Difficulty'] = ""
    
    # Sort by difficulty (exercises only)
    exercise_rows = [e for e in exercises if e['Type'] == 'Exercise']
    contest_rows = [e for e in exercises if e['Type'] != 'Exercise']
    
    exercise_rows.sort(key=lambda x: int(x['Difficulty']) if str(x['Difficulty']).isdigit() else 999)
    
    # Write updated CSV
    fieldnames = ['Day', 'Type', 'Problem_Name', 'Contest_Name', 'Problem_Link', 'Contest_Link', 'PDF_Link', 'Category', 'Difficulty']
    
    with open('exercises_list_updated.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        # Write sorted exercises
        for exercise in exercise_rows:
            writer.writerow(exercise)
        
        # Write contests
        for contest in contest_rows:
            writer.writerow(contest)
    
    print(f"Updated {len(exercise_rows)} exercises")
    print("Created exercises_list_updated.csv")

if __name__ == "__main__":
    update_exercises_csv()
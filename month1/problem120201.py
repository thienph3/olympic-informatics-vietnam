"""
Problem 120201: File operations cơ bản
Read/write text files, handle different encodings, process large files

Bài 1: Basic File Operations
- Read và write text files
- Handle different file modes
- File encoding issues

Bài 2: Advanced File Processing
- Process large files efficiently
- Batch file operations
- File system utilities
"""

import os
import sys
import time
from pathlib import Path
import tempfile
import shutil

# Basic File Operations
def basic_file_operations():
    """Demonstrate basic file read/write operations"""
    print("=== Basic File Operations ===")
    
    # Create sample data
    sample_data = """Line 1: Hello World
Line 2: Python File I/O
Line 3: Olympic Programming
Line 4: 2024 Contest
Line 5: Final Line"""
    
    filename = "sample_data.txt"
    
    # Write to file
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(sample_data)
        print(f"✓ Successfully wrote to {filename}")
    except IOError as e:
        print(f"✗ Error writing file: {e}")
        return
    
    # Read entire file
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"✓ Read {len(content)} characters")
        print("First 50 characters:", repr(content[:50]))
    except IOError as e:
        print(f"✗ Error reading file: {e}")
    
    # Read line by line
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = []
            for i, line in enumerate(file, 1):
                lines.append(line.strip())
                if i <= 3:  # Show first 3 lines
                    print(f"Line {i}: {line.strip()}")
        print(f"✓ Read {len(lines)} lines total")
    except IOError as e:
        print(f"✗ Error reading lines: {e}")
    
    # Read all lines at once
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            all_lines = file.readlines()
        print(f"✓ Read all lines: {len(all_lines)} lines")
    except IOError as e:
        print(f"✗ Error reading all lines: {e}")
    
    # Append to file
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write("\nLine 6: Appended line")
        print("✓ Successfully appended to file")
    except IOError as e:
        print(f"✗ Error appending: {e}")
    
    # Clean up
    try:
        os.remove(filename)
        print(f"✓ Cleaned up {filename}")
    except OSError as e:
        print(f"✗ Error cleaning up: {e}")

def file_modes_demo():
    """Demonstrate different file modes"""
    print("\n=== File Modes Demo ===")
    
    filename = "modes_test.txt"
    
    # Mode 'w' - write (overwrite)
    with open(filename, 'w') as f:
        f.write("Original content\n")
    print("✓ Written with mode 'w'")
    
    # Mode 'a' - append
    with open(filename, 'a') as f:
        f.write("Appended content\n")
    print("✓ Appended with mode 'a'")
    
    # Mode 'r+' - read and write
    with open(filename, 'r+') as f:
        content = f.read()
        f.write("Added at end\n")
    print("✓ Read and wrote with mode 'r+'")
    
    # Mode 'x' - exclusive creation (fails if file exists)
    try:
        with open("new_file.txt", 'x') as f:
            f.write("Exclusive creation\n")
        print("✓ Created with mode 'x'")
        os.remove("new_file.txt")
    except FileExistsError:
        print("✗ File already exists (mode 'x')")
    
    # Read final content
    with open(filename, 'r') as f:
        final_content = f.read()
    print(f"Final content ({len(final_content)} chars):")
    print(repr(final_content))
    
    # Clean up
    os.remove(filename)

def encoding_handling():
    """Demonstrate encoding handling"""
    print("\n=== Encoding Handling ===")
    
    # Test different encodings
    test_text = "Hello World! Xin chào! 你好! こんにちは! 🌍"
    
    encodings = ['utf-8', 'utf-16', 'ascii', 'latin-1']
    
    for encoding in encodings:
        filename = f"test_{encoding.replace('-', '_')}.txt"
        
        try:
            # Write with specific encoding
            with open(filename, 'w', encoding=encoding) as f:
                f.write(test_text)
            
            # Read back
            with open(filename, 'r', encoding=encoding) as f:
                read_text = f.read()
            
            # Check if content matches
            if read_text == test_text:
                print(f"✓ {encoding}: Successfully handled")
            else:
                print(f"✗ {encoding}: Content mismatch")
            
            # Show file size
            size = os.path.getsize(filename)
            print(f"  File size: {size} bytes")
            
            os.remove(filename)
            
        except UnicodeEncodeError as e:
            print(f"✗ {encoding}: Encode error - {e}")
        except UnicodeDecodeError as e:
            print(f"✗ {encoding}: Decode error - {e}")
        except Exception as e:
            print(f"✗ {encoding}: Other error - {e}")

def binary_file_operations():
    """Demonstrate binary file operations"""
    print("\n=== Binary File Operations ===")
    
    # Create binary data
    binary_data = bytes(range(256))  # 0-255
    filename = "binary_test.bin"
    
    # Write binary data
    try:
        with open(filename, 'wb') as f:
            f.write(binary_data)
        print(f"✓ Written {len(binary_data)} bytes")
    except IOError as e:
        print(f"✗ Error writing binary: {e}")
        return
    
    # Read binary data
    try:
        with open(filename, 'rb') as f:
            read_data = f.read()
        
        print(f"✓ Read {len(read_data)} bytes")
        print(f"First 10 bytes: {list(read_data[:10])}")
        print(f"Last 10 bytes: {list(read_data[-10:])}")
        
        # Verify data integrity
        if read_data == binary_data:
            print("✓ Binary data integrity verified")
        else:
            print("✗ Binary data corrupted")
            
    except IOError as e:
        print(f"✗ Error reading binary: {e}")
    
    # Read chunks
    try:
        with open(filename, 'rb') as f:
            chunk_size = 64
            chunks = []
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                chunks.append(chunk)
        
        print(f"✓ Read in {len(chunks)} chunks of {chunk_size} bytes")
        
    except IOError as e:
        print(f"✗ Error reading chunks: {e}")
    
    # Clean up
    os.remove(filename)

def large_file_processing():
    """Demonstrate efficient large file processing"""
    print("\n=== Large File Processing ===")
    
    # Create a large file for testing
    large_filename = "large_test.txt"
    num_lines = 10000
    
    print(f"Creating large file with {num_lines} lines...")
    start_time = time.time()
    
    try:
        with open(large_filename, 'w') as f:
            for i in range(num_lines):
                f.write(f"Line {i+1}: This is line number {i+1} with some sample data.\n")
        
        creation_time = time.time() - start_time
        file_size = os.path.getsize(large_filename)
        print(f"✓ Created {file_size:,} byte file in {creation_time:.3f}s")
        
    except IOError as e:
        print(f"✗ Error creating large file: {e}")
        return
    
    # Method 1: Read entire file (memory intensive)
    start_time = time.time()
    try:
        with open(large_filename, 'r') as f:
            all_content = f.read()
        
        read_time = time.time() - start_time
        print(f"✓ Read entire file ({len(all_content):,} chars) in {read_time:.3f}s")
        
    except MemoryError:
        print("✗ Not enough memory to read entire file")
    except IOError as e:
        print(f"✗ Error reading entire file: {e}")
    
    # Method 2: Process line by line (memory efficient)
    start_time = time.time()
    line_count = 0
    word_count = 0
    
    try:
        with open(large_filename, 'r') as f:
            for line in f:
                line_count += 1
                word_count += len(line.split())
        
        process_time = time.time() - start_time
        print(f"✓ Processed {line_count:,} lines ({word_count:,} words) in {process_time:.3f}s")
        
    except IOError as e:
        print(f"✗ Error processing line by line: {e}")
    
    # Method 3: Process in chunks
    start_time = time.time()
    chunk_size = 8192  # 8KB chunks
    total_chars = 0
    chunk_count = 0
    
    try:
        with open(large_filename, 'r') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                total_chars += len(chunk)
                chunk_count += 1
        
        chunk_time = time.time() - start_time
        print(f"✓ Processed {chunk_count} chunks ({total_chars:,} chars) in {chunk_time:.3f}s")
        
    except IOError as e:
        print(f"✗ Error processing chunks: {e}")
    
    # Clean up
    os.remove(large_filename)

def file_system_utilities():
    """Demonstrate file system utility functions"""
    print("\n=== File System Utilities ===")
    
    # Create test directory structure
    test_dir = "test_directory"
    
    try:
        os.makedirs(test_dir, exist_ok=True)
        print(f"✓ Created directory: {test_dir}")
        
        # Create some test files
        test_files = []
        for i in range(3):
            filename = os.path.join(test_dir, f"file_{i}.txt")
            with open(filename, 'w') as f:
                f.write(f"Content of file {i}\n" * (i + 1))
            test_files.append(filename)
        
        print(f"✓ Created {len(test_files)} test files")
        
        # List directory contents
        contents = os.listdir(test_dir)
        print(f"Directory contents: {contents}")
        
        # Get file information
        for filename in test_files:
            stat_info = os.stat(filename)
            print(f"  {os.path.basename(filename)}:")
            print(f"    Size: {stat_info.st_size} bytes")
            print(f"    Modified: {time.ctime(stat_info.st_mtime)}")
        
        # Copy file
        source = test_files[0]
        destination = os.path.join(test_dir, "copied_file.txt")
        shutil.copy2(source, destination)
        print(f"✓ Copied {source} to {destination}")
        
        # Move file
        old_path = destination
        new_path = os.path.join(test_dir, "moved_file.txt")
        shutil.move(old_path, new_path)
        print(f"✓ Moved {old_path} to {new_path}")
        
        # Calculate directory size
        total_size = 0
        for root, dirs, files in os.walk(test_dir):
            for file in files:
                filepath = os.path.join(root, file)
                total_size += os.path.getsize(filepath)
        
        print(f"✓ Total directory size: {total_size} bytes")
        
    except Exception as e:
        print(f"✗ Error in file system operations: {e}")
    
    finally:
        # Clean up
        try:
            shutil.rmtree(test_dir)
            print(f"✓ Cleaned up {test_dir}")
        except Exception as e:
            print(f"✗ Error cleaning up: {e}")

def temporary_files_demo():
    """Demonstrate temporary file operations"""
    print("\n=== Temporary Files Demo ===")
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_file:
        temp_filename = temp_file.name
        temp_file.write("Temporary file content\n")
        temp_file.write("This will be deleted automatically\n")
        print(f"✓ Created temporary file: {temp_filename}")
    
    # Read from temporary file
    try:
        with open(temp_filename, 'r') as f:
            content = f.read()
        print(f"✓ Read from temp file: {len(content)} characters")
    except IOError as e:
        print(f"✗ Error reading temp file: {e}")
    
    # Clean up temporary file
    try:
        os.unlink(temp_filename)
        print("✓ Cleaned up temporary file")
    except OSError as e:
        print(f"✗ Error cleaning temp file: {e}")
    
    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"✓ Created temporary directory: {temp_dir}")
        
        # Create files in temp directory
        for i in range(3):
            temp_file_path = os.path.join(temp_dir, f"temp_{i}.txt")
            with open(temp_file_path, 'w') as f:
                f.write(f"Temporary file {i}\n")
        
        # List temp directory
        temp_contents = os.listdir(temp_dir)
        print(f"✓ Temp directory contains: {temp_contents}")
    
    print("✓ Temporary directory automatically cleaned up")

def safe_file_operations():
    """Demonstrate safe file operation patterns"""
    print("\n=== Safe File Operations ===")
    
    def safe_write_file(filename, content):
        """Safely write to file with backup"""
        backup_filename = filename + ".backup"
        
        try:
            # Create backup if original exists
            if os.path.exists(filename):
                shutil.copy2(filename, backup_filename)
                print(f"✓ Created backup: {backup_filename}")
            
            # Write to temporary file first
            temp_filename = filename + ".tmp"
            with open(temp_filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Atomic move (on most systems)
            shutil.move(temp_filename, filename)
            print(f"✓ Safely wrote to {filename}")
            
            # Remove backup on success
            if os.path.exists(backup_filename):
                os.remove(backup_filename)
                print("✓ Removed backup after successful write")
            
            return True
            
        except Exception as e:
            print(f"✗ Error writing file: {e}")
            
            # Restore from backup if available
            if os.path.exists(backup_filename):
                shutil.move(backup_filename, filename)
                print("✓ Restored from backup")
            
            # Clean up temp file
            if os.path.exists(temp_filename):
                os.remove(temp_filename)
            
            return False
    
    # Test safe write
    test_filename = "safe_test.txt"
    test_content = "This is a test of safe file writing.\nMultiple lines of content.\n"
    
    success = safe_write_file(test_filename, test_content)
    if success:
        # Verify content
        with open(test_filename, 'r') as f:
            read_content = f.read()
        
        if read_content == test_content:
            print("✓ Content verification passed")
        else:
            print("✗ Content verification failed")
        
        # Clean up
        os.remove(test_filename)

# Test all functions
if __name__ == "__main__":
    basic_file_operations()
    file_modes_demo()
    encoding_handling()
    binary_file_operations()
    large_file_processing()
    file_system_utilities()
    temporary_files_demo()
    safe_file_operations()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Build file backup system với versioning")
    print("2. Create log file analyzer")
    print("3. Implement file synchronization tool")
    print("4. Build text file merger với conflict resolution")
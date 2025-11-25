"""
Problem 120302: Robust file processing
Build robust file processing với comprehensive error handling

Bài 1: Safe File Operations
- Atomic file operations
- Backup và recovery
- File locking simulation

Bài 2: Batch File Processing
- Process multiple files
- Error recovery strategies
- Progress tracking
"""

import os
import shutil
import tempfile
import json
import csv
import time
import hashlib
from pathlib import Path
from typing import List, Dict, Any, Optional, Callable
from contextlib import contextmanager

# Safe File Operations
class FileOperationError(Exception):
    """Custom exception for file operations"""
    def __init__(self, message, filename=None, operation=None):
        self.message = message
        self.filename = filename
        self.operation = operation
        super().__init__(self.message)
    
    def __str__(self):
        base_msg = f"File operation error: {self.message}"
        if self.filename:
            base_msg += f" (file: {self.filename})"
        if self.operation:
            base_msg += f" (operation: {self.operation})"
        return base_msg

class SafeFileWriter:
    """Safe file writer with atomic operations and backup"""
    
    def __init__(self, filename, backup=True, encoding='utf-8'):
        self.filename = filename
        self.backup = backup
        self.encoding = encoding
        self.backup_filename = None
        self.temp_filename = None
    
    def __enter__(self):
        try:
            # Create backup if file exists
            if self.backup and os.path.exists(self.filename):
                self.backup_filename = self.filename + '.backup'
                shutil.copy2(self.filename, self.backup_filename)
            
            # Create temporary file
            self.temp_filename = self.filename + '.tmp'
            self.file_handle = open(self.temp_filename, 'w', encoding=self.encoding)
            
            return self.file_handle
            
        except Exception as e:
            self._cleanup()
            raise FileOperationError(f"Failed to initialize safe writer: {e}", 
                                   self.filename, "initialize")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if self.file_handle:
                self.file_handle.close()
            
            if exc_type is None:
                # Success: move temp file to final location
                shutil.move(self.temp_filename, self.filename)
                
                # Remove backup on success
                if self.backup_filename and os.path.exists(self.backup_filename):
                    os.remove(self.backup_filename)
                
                return True
            else:
                # Error occurred: restore from backup if available
                if self.backup_filename and os.path.exists(self.backup_filename):
                    shutil.move(self.backup_filename, self.filename)
                
                self._cleanup()
                return False
                
        except Exception as cleanup_error:
            print(f"Warning: Cleanup error: {cleanup_error}")
            return False
    
    def _cleanup(self):
        """Clean up temporary files"""
        if self.temp_filename and os.path.exists(self.temp_filename):
            try:
                os.remove(self.temp_filename)
            except OSError:
                pass

def safe_file_operations_demo():
    """Demonstrate safe file operations"""
    print("=== Safe File Operations Demo ===")
    
    # Test successful write
    test_file = "safe_test.txt"
    test_content = "This is test content\nLine 2\nLine 3\n"
    
    try:
        with SafeFileWriter(test_file) as f:
            f.write(test_content)
        
        # Verify content
        with open(test_file, 'r') as f:
            read_content = f.read()
        
        if read_content == test_content:
            print("✓ Safe write successful")
        else:
            print("✗ Content verification failed")
            
    except FileOperationError as e:
        print(f"✗ Safe write failed: {e}")
    
    # Test write with simulated error
    try:
        with SafeFileWriter(test_file) as f:
            f.write("Partial content\n")
            # Simulate error
            raise ValueError("Simulated write error")
        
    except ValueError:
        print("✓ Error handling worked - file should be restored")
        
        # Verify original content is preserved
        try:
            with open(test_file, 'r') as f:
                content = f.read()
            if content == test_content:
                print("✓ Original content preserved after error")
            else:
                print("✗ Content was corrupted")
        except FileNotFoundError:
            print("✗ File was lost during error")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)

@contextmanager
def file_lock_simulation(filename, timeout=5):
    """Simulate file locking mechanism"""
    lock_file = filename + '.lock'
    start_time = time.time()
    
    # Wait for lock to be available
    while os.path.exists(lock_file):
        if time.time() - start_time > timeout:
            raise FileOperationError(f"Timeout waiting for file lock", filename, "lock")
        time.sleep(0.1)
    
    try:
        # Create lock file
        with open(lock_file, 'w') as f:
            f.write(str(os.getpid()))
        
        yield filename
        
    finally:
        # Remove lock file
        try:
            os.remove(lock_file)
        except OSError:
            pass

def file_locking_demo():
    """Demonstrate file locking simulation"""
    print("\n=== File Locking Demo ===")
    
    test_file = "locked_file.txt"
    
    try:
        # First process gets the lock
        with file_lock_simulation(test_file) as locked_file:
            print(f"✓ Acquired lock for {locked_file}")
            
            # Write to file safely
            with open(locked_file, 'w') as f:
                f.write("Content written with lock protection\n")
            
            print("✓ File written successfully")
        
        print("✓ Lock released")
        
        # Verify content
        with open(test_file, 'r') as f:
            content = f.read()
        print(f"✓ File content: {repr(content.strip())}")
        
    except FileOperationError as e:
        print(f"✗ File locking error: {e}")
    
    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)

def file_integrity_check():
    """Demonstrate file integrity checking"""
    print("\n=== File Integrity Check ===")
    
    def calculate_file_hash(filename):
        """Calculate SHA-256 hash of file"""
        hash_sha256 = hashlib.sha256()
        try:
            with open(filename, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
        except IOError as e:
            raise FileOperationError(f"Cannot calculate hash: {e}", filename, "hash")
    
    def write_with_integrity_check(filename, content):
        """Write file with integrity verification"""
        try:
            # Write content
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Calculate and store hash
            file_hash = calculate_file_hash(filename)
            hash_file = filename + '.sha256'
            
            with open(hash_file, 'w') as f:
                f.write(f"{file_hash}  {filename}\n")
            
            return file_hash
            
        except Exception as e:
            raise FileOperationError(f"Write with integrity check failed: {e}", 
                                   filename, "write_with_check")
    
    def verify_file_integrity(filename):
        """Verify file integrity using stored hash"""
        hash_file = filename + '.sha256'
        
        try:
            # Read stored hash
            with open(hash_file, 'r') as f:
                stored_hash = f.read().strip().split()[0]
            
            # Calculate current hash
            current_hash = calculate_file_hash(filename)
            
            return stored_hash == current_hash, stored_hash, current_hash
            
        except Exception as e:
            raise FileOperationError(f"Integrity verification failed: {e}", 
                                   filename, "verify")
    
    # Test integrity checking
    test_file = "integrity_test.txt"
    test_content = "This content will be integrity checked\n" * 100
    
    try:
        # Write with integrity check
        original_hash = write_with_integrity_check(test_file, test_content)
        print(f"✓ File written with hash: {original_hash[:16]}...")
        
        # Verify integrity
        is_valid, stored, current = verify_file_integrity(test_file)
        if is_valid:
            print("✓ File integrity verified")
        else:
            print(f"✗ File integrity check failed")
            print(f"  Stored:  {stored[:16]}...")
            print(f"  Current: {current[:16]}...")
        
        # Simulate file corruption
        with open(test_file, 'a') as f:
            f.write("CORRUPTED DATA")
        
        # Verify again
        is_valid, stored, current = verify_file_integrity(test_file)
        if not is_valid:
            print("✓ Corruption detected successfully")
        else:
            print("✗ Failed to detect corruption")
        
    except FileOperationError as e:
        print(f"✗ Integrity check error: {e}")
    
    # Clean up
    for ext in ['', '.sha256']:
        filename = test_file + ext
        if os.path.exists(filename):
            os.remove(filename)

# Batch File Processing
class BatchProcessor:
    """Batch file processor with error handling and progress tracking"""
    
    def __init__(self, error_strategy='continue'):
        """
        Initialize batch processor
        
        Args:
            error_strategy: 'continue', 'stop', or 'retry'
        """
        self.error_strategy = error_strategy
        self.results = []
        self.errors = []
        self.processed_count = 0
        self.total_count = 0
    
    def process_files(self, file_list: List[str], processor_func: Callable, 
                     progress_callback: Optional[Callable] = None):
        """Process multiple files with error handling"""
        self.total_count = len(file_list)
        self.processed_count = 0
        self.results.clear()
        self.errors.clear()
        
        for i, filename in enumerate(file_list):
            try:
                # Process single file
                result = self._process_single_file(filename, processor_func)
                self.results.append({
                    'filename': filename,
                    'status': 'success',
                    'result': result
                })
                
            except Exception as e:
                error_info = {
                    'filename': filename,
                    'status': 'error',
                    'error': str(e),
                    'error_type': type(e).__name__
                }
                self.errors.append(error_info)
                self.results.append(error_info)
                
                # Handle error based on strategy
                if self.error_strategy == 'stop':
                    print(f"✗ Stopping batch processing due to error in {filename}: {e}")
                    break
                elif self.error_strategy == 'retry':
                    # Simple retry logic
                    try:
                        print(f"Retrying {filename}...")
                        result = self._process_single_file(filename, processor_func)
                        self.results[-1] = {
                            'filename': filename,
                            'status': 'success_retry',
                            'result': result
                        }
                        # Remove from errors list
                        self.errors.pop()
                    except Exception as retry_error:
                        print(f"✗ Retry failed for {filename}: {retry_error}")
            
            self.processed_count += 1
            
            # Progress callback
            if progress_callback:
                progress_callback(self.processed_count, self.total_count, filename)
        
        return self.results
    
    def _process_single_file(self, filename: str, processor_func: Callable):
        """Process a single file"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        
        return processor_func(filename)
    
    def get_summary(self):
        """Get processing summary"""
        success_count = sum(1 for r in self.results if r['status'].startswith('success'))
        error_count = len(self.errors)
        
        return {
            'total': self.total_count,
            'processed': self.processed_count,
            'success': success_count,
            'errors': error_count,
            'success_rate': success_count / self.total_count if self.total_count > 0 else 0
        }

def batch_processing_demo():
    """Demonstrate batch file processing"""
    print("\n=== Batch Processing Demo ===")
    
    # Create test files
    test_files = []
    test_dir = "batch_test"
    os.makedirs(test_dir, exist_ok=True)
    
    try:
        # Create various test files
        file_contents = [
            ("file1.txt", "Content of file 1\nLine 2\n"),
            ("file2.json", '{"name": "test", "value": 123}'),
            ("file3.csv", "name,age,city\nAlice,25,NYC\nBob,30,LA\n"),
            ("file4.txt", "Another text file\n"),
            ("corrupted.json", '{"invalid": json,}'),  # Invalid JSON
        ]
        
        for filename, content in file_contents:
            filepath = os.path.join(test_dir, filename)
            with open(filepath, 'w') as f:
                f.write(content)
            test_files.append(filepath)
        
        # Add non-existent file to test error handling
        test_files.append(os.path.join(test_dir, "nonexistent.txt"))
        
        # Define file processors
        def count_lines(filename):
            """Count lines in a text file"""
            with open(filename, 'r') as f:
                return len(f.readlines())
        
        def validate_json(filename):
            """Validate JSON file"""
            with open(filename, 'r') as f:
                data = json.load(f)
            return f"Valid JSON with {len(data)} keys"
        
        def get_file_info(filename):
            """Get basic file information"""
            stat = os.stat(filename)
            return {
                'size': stat.st_size,
                'modified': time.ctime(stat.st_mtime)
            }
        
        # Progress callback
        def progress_callback(current, total, filename):
            percentage = (current / total) * 100
            print(f"Progress: {current}/{total} ({percentage:.1f}%) - {os.path.basename(filename)}")
        
        # Test different error strategies
        strategies = ['continue', 'stop', 'retry']
        
        for strategy in strategies:
            print(f"\n--- Testing strategy: {strategy} ---")
            
            processor = BatchProcessor(error_strategy=strategy)
            results = processor.process_files(
                test_files, 
                get_file_info, 
                progress_callback
            )
            
            summary = processor.get_summary()
            print(f"Summary: {summary['success']}/{summary['total']} successful "
                  f"({summary['success_rate']:.1%} success rate)")
            
            if processor.errors:
                print("Errors encountered:")
                for error in processor.errors:
                    print(f"  {error['filename']}: {error['error']}")
    
    finally:
        # Clean up
        shutil.rmtree(test_dir, ignore_errors=True)

def data_migration_demo():
    """Demonstrate data migration with error handling"""
    print("\n=== Data Migration Demo ===")
    
    class DataMigrator:
        """Data migrator with comprehensive error handling"""
        
        def __init__(self):
            self.migration_log = []
            self.rollback_info = []
        
        def migrate_csv_to_json(self, csv_file, json_file):
            """Migrate CSV data to JSON format"""
            try:
                # Read CSV
                with open(csv_file, 'r') as f:
                    reader = csv.DictReader(f)
                    data = list(reader)
                
                # Backup existing JSON file if it exists
                if os.path.exists(json_file):
                    backup_file = json_file + '.backup'
                    shutil.copy2(json_file, backup_file)
                    self.rollback_info.append(('restore', json_file, backup_file))
                else:
                    self.rollback_info.append(('delete', json_file, None))
                
                # Write JSON
                with SafeFileWriter(json_file) as f:
                    json.dump(data, f, indent=2)
                
                self.migration_log.append(f"✓ Migrated {csv_file} → {json_file}")
                return True
                
            except Exception as e:
                self.migration_log.append(f"✗ Migration failed {csv_file} → {json_file}: {e}")
                return False
        
        def rollback_migration(self):
            """Rollback migration changes"""
            print("Rolling back migration...")
            
            for action, target_file, source_file in reversed(self.rollback_info):
                try:
                    if action == 'restore' and source_file:
                        shutil.move(source_file, target_file)
                        print(f"✓ Restored {target_file}")
                    elif action == 'delete':
                        if os.path.exists(target_file):
                            os.remove(target_file)
                            print(f"✓ Removed {target_file}")
                except Exception as e:
                    print(f"✗ Rollback error for {target_file}: {e}")
            
            self.rollback_info.clear()
        
        def get_migration_log(self):
            """Get migration log"""
            return self.migration_log.copy()
    
    # Create test data
    test_dir = "migration_test"
    os.makedirs(test_dir, exist_ok=True)
    
    try:
        # Create test CSV files
        csv_files = [
            ("users.csv", [
                ["name", "age", "city"],
                ["Alice", "25", "NYC"],
                ["Bob", "30", "LA"]
            ]),
            ("products.csv", [
                ["name", "price", "category"],
                ["Laptop", "1200", "Electronics"],
                ["Book", "15", "Education"]
            ])
        ]
        
        for filename, data in csv_files:
            filepath = os.path.join(test_dir, filename)
            with open(filepath, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        
        # Perform migration
        migrator = DataMigrator()
        
        for csv_filename, _ in csv_files:
            csv_path = os.path.join(test_dir, csv_filename)
            json_path = os.path.join(test_dir, csv_filename.replace('.csv', '.json'))
            
            success = migrator.migrate_csv_to_json(csv_path, json_path)
            
            if success:
                # Verify migration
                with open(json_path, 'r') as f:
                    migrated_data = json.load(f)
                print(f"✓ Migrated {len(migrated_data)} records to {json_path}")
        
        # Show migration log
        print("\nMigration log:")
        for entry in migrator.get_migration_log():
            print(f"  {entry}")
        
        # Simulate error and rollback
        print("\nSimulating error and rollback...")
        migrator.rollback_migration()
        
    finally:
        # Clean up
        shutil.rmtree(test_dir, ignore_errors=True)

# Test all functions
if __name__ == "__main__":
    safe_file_operations_demo()
    file_locking_demo()
    file_integrity_check()
    batch_processing_demo()
    data_migration_demo()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Build file synchronization system với conflict resolution")
    print("2. Create backup system với incremental backups")
    print("3. Implement log file rotation với compression")
    print("4. Build data validation pipeline với error reporting")
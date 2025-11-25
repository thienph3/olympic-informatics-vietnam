"""
Problem 120402: Olympic problem solver với error handling
Build complete Olympic problem solver với robust error handling

Bài 1: Problem Input/Output Handler
- Parse problem input safely
- Validate constraints
- Format output correctly

Bài 2: Complete Problem Solver Framework
- Modular solution architecture
- Error recovery strategies
- Performance monitoring
"""

import os
import sys
import time
import json
import traceback
from typing import Any, Dict, List, Optional, Tuple, Callable
from dataclasses import dataclass
from enum import Enum

# Problem Solver Framework
class ProblemType(Enum):
    """Types of Olympic problems"""
    MATH = "mathematics"
    GRAPH = "graph_theory"
    DP = "dynamic_programming"
    GREEDY = "greedy"
    STRING = "string_processing"
    GEOMETRY = "geometry"

class SolutionStatus(Enum):
    """Solution execution status"""
    SUCCESS = "success"
    WRONG_ANSWER = "wrong_answer"
    TIME_LIMIT = "time_limit_exceeded"
    MEMORY_LIMIT = "memory_limit_exceeded"
    RUNTIME_ERROR = "runtime_error"
    COMPILATION_ERROR = "compilation_error"
    INPUT_ERROR = "input_error"

@dataclass
class TestCase:
    """Test case data structure"""
    input_data: str
    expected_output: str
    time_limit: float = 1.0
    memory_limit: int = 256  # MB
    description: str = ""

@dataclass
class SolutionResult:
    """Solution execution result"""
    status: SolutionStatus
    output: str = ""
    execution_time: float = 0.0
    memory_used: int = 0
    error_message: str = ""
    traceback_info: str = ""

class InputParser:
    """Safe input parser for Olympic problems"""
    
    def __init__(self, input_text: str):
        self.lines = input_text.strip().split('\n')
        self.current_line = 0
    
    def read_int(self) -> int:
        """Read single integer"""
        try:
            if self.current_line >= len(self.lines):
                raise ValueError("No more input lines available")
            
            value = int(self.lines[self.current_line].strip())
            self.current_line += 1
            return value
            
        except ValueError as e:
            raise ValueError(f"Cannot parse integer from line {self.current_line + 1}: {e}")
    
    def read_ints(self) -> List[int]:
        """Read multiple integers from current line"""
        try:
            if self.current_line >= len(self.lines):
                raise ValueError("No more input lines available")
            
            values = list(map(int, self.lines[self.current_line].strip().split()))
            self.current_line += 1
            return values
            
        except ValueError as e:
            raise ValueError(f"Cannot parse integers from line {self.current_line + 1}: {e}")
    
    def read_string(self) -> str:
        """Read string from current line"""
        try:
            if self.current_line >= len(self.lines):
                raise ValueError("No more input lines available")
            
            value = self.lines[self.current_line].strip()
            self.current_line += 1
            return value
            
        except Exception as e:
            raise ValueError(f"Cannot read string from line {self.current_line + 1}: {e}")
    
    def read_matrix(self, rows: int, cols: int) -> List[List[int]]:
        """Read integer matrix"""
        try:
            matrix = []
            for i in range(rows):
                row = self.read_ints()
                if len(row) != cols:
                    raise ValueError(f"Row {i + 1} has {len(row)} elements, expected {cols}")
                matrix.append(row)
            return matrix
            
        except Exception as e:
            raise ValueError(f"Cannot read matrix: {e}")
    
    def has_more_lines(self) -> bool:
        """Check if more input lines are available"""
        return self.current_line < len(self.lines)

class ConstraintValidator:
    """Validate problem constraints"""
    
    @staticmethod
    def validate_range(value: int, min_val: int, max_val: int, name: str = "value"):
        """Validate integer is in range"""
        if not (min_val <= value <= max_val):
            raise ValueError(f"{name} {value} is not in range [{min_val}, {max_val}]")
    
    @staticmethod
    def validate_array_size(arr: List, min_size: int, max_size: int, name: str = "array"):
        """Validate array size"""
        size = len(arr)
        if not (min_size <= size <= max_size):
            raise ValueError(f"{name} size {size} is not in range [{min_size}, {max_size}]")
    
    @staticmethod
    def validate_string_length(s: str, min_len: int, max_len: int, name: str = "string"):
        """Validate string length"""
        length = len(s)
        if not (min_len <= length <= max_len):
            raise ValueError(f"{name} length {length} is not in range [{min_len}, {max_len}]")
    
    @staticmethod
    def validate_all_positive(arr: List[int], name: str = "array"):
        """Validate all elements are positive"""
        for i, val in enumerate(arr):
            if val <= 0:
                raise ValueError(f"{name}[{i}] = {val} is not positive")

class OlympicProblem:
    """Base class for Olympic problems"""
    
    def __init__(self, problem_id: str, problem_type: ProblemType):
        self.problem_id = problem_id
        self.problem_type = problem_type
        self.test_cases: List[TestCase] = []
    
    def parse_input(self, input_text: str) -> Any:
        """Parse problem input - to be overridden"""
        raise NotImplementedError("Subclasses must implement parse_input")
    
    def solve(self, parsed_input: Any) -> Any:
        """Solve the problem - to be overridden"""
        raise NotImplementedError("Subclasses must implement solve")
    
    def format_output(self, result: Any) -> str:
        """Format solution output - to be overridden"""
        raise NotImplementedError("Subclasses must implement format_output")
    
    def add_test_case(self, input_data: str, expected_output: str, 
                     time_limit: float = 1.0, description: str = ""):
        """Add test case"""
        test_case = TestCase(input_data, expected_output, time_limit, description)
        self.test_cases.append(test_case)

class SumProblem(OlympicProblem):
    """Example: Simple sum problem"""
    
    def __init__(self):
        super().__init__("SUM001", ProblemType.MATH)
    
    def parse_input(self, input_text: str) -> Tuple[int, List[int]]:
        """Parse input: first line n, second line n integers"""
        parser = InputParser(input_text)
        
        n = parser.read_int()
        ConstraintValidator.validate_range(n, 1, 100000, "n")
        
        numbers = parser.read_ints()
        ConstraintValidator.validate_array_size(numbers, n, n, "numbers array")
        
        # Validate each number
        for i, num in enumerate(numbers):
            ConstraintValidator.validate_range(num, -1000000, 1000000, f"numbers[{i}]")
        
        return n, numbers
    
    def solve(self, parsed_input: Tuple[int, List[int]]) -> int:
        """Solve: return sum of numbers"""
        n, numbers = parsed_input
        return sum(numbers)
    
    def format_output(self, result: int) -> str:
        """Format output: single integer"""
        return str(result)

class PalindromeProblem(OlympicProblem):
    """Example: Palindrome checking problem"""
    
    def __init__(self):
        super().__init__("STR001", ProblemType.STRING)
    
    def parse_input(self, input_text: str) -> str:
        """Parse input: single string"""
        parser = InputParser(input_text)
        
        s = parser.read_string()
        ConstraintValidator.validate_string_length(s, 1, 100000, "input string")
        
        # Validate only contains letters and digits
        if not s.isalnum():
            raise ValueError("String must contain only letters and digits")
        
        return s
    
    def solve(self, parsed_input: str) -> bool:
        """Solve: check if string is palindrome"""
        s = parsed_input.lower()
        return s == s[::-1]
    
    def format_output(self, result: bool) -> str:
        """Format output: YES or NO"""
        return "YES" if result else "NO"

class FibonacciProblem(OlympicProblem):
    """Example: Fibonacci number problem"""
    
    def __init__(self):
        super().__init__("DP001", ProblemType.DP)
        self.memo = {}
    
    def parse_input(self, input_text: str) -> int:
        """Parse input: single integer n"""
        parser = InputParser(input_text)
        
        n = parser.read_int()
        ConstraintValidator.validate_range(n, 0, 50, "n")
        
        return n
    
    def solve(self, parsed_input: int) -> int:
        """Solve: return nth Fibonacci number with memoization"""
        n = parsed_input
        
        if n in self.memo:
            return self.memo[n]
        
        if n <= 1:
            result = n
        else:
            result = self.solve(n - 1) + self.solve(n - 2)
        
        self.memo[n] = result
        return result
    
    def format_output(self, result: int) -> str:
        """Format output: single integer"""
        return str(result)

class ProblemSolver:
    """Main problem solver with error handling"""
    
    def __init__(self):
        self.problems: Dict[str, OlympicProblem] = {}
        self.execution_log: List[Dict] = []
    
    def register_problem(self, problem: OlympicProblem):
        """Register a problem"""
        self.problems[problem.problem_id] = problem
    
    def solve_problem(self, problem_id: str, input_text: str, 
                     time_limit: float = 1.0) -> SolutionResult:
        """Solve a problem with comprehensive error handling"""
        start_time = time.time()
        
        try:
            # Get problem
            if problem_id not in self.problems:
                return SolutionResult(
                    status=SolutionStatus.COMPILATION_ERROR,
                    error_message=f"Problem {problem_id} not found"
                )
            
            problem = self.problems[problem_id]
            
            # Parse input
            try:
                parsed_input = problem.parse_input(input_text)
            except Exception as e:
                return SolutionResult(
                    status=SolutionStatus.INPUT_ERROR,
                    error_message=f"Input parsing error: {e}",
                    traceback_info=traceback.format_exc()
                )
            
            # Solve with time limit
            try:
                solution_start = time.time()
                result = problem.solve(parsed_input)
                solution_time = time.time() - solution_start
                
                if solution_time > time_limit:
                    return SolutionResult(
                        status=SolutionStatus.TIME_LIMIT,
                        execution_time=solution_time,
                        error_message=f"Time limit exceeded: {solution_time:.3f}s > {time_limit}s"
                    )
                
            except Exception as e:
                return SolutionResult(
                    status=SolutionStatus.RUNTIME_ERROR,
                    execution_time=time.time() - solution_start,
                    error_message=f"Runtime error: {e}",
                    traceback_info=traceback.format_exc()
                )
            
            # Format output
            try:
                output = problem.format_output(result)
            except Exception as e:
                return SolutionResult(
                    status=SolutionStatus.RUNTIME_ERROR,
                    execution_time=time.time() - start_time,
                    error_message=f"Output formatting error: {e}",
                    traceback_info=traceback.format_exc()
                )
            
            # Success
            total_time = time.time() - start_time
            return SolutionResult(
                status=SolutionStatus.SUCCESS,
                output=output,
                execution_time=total_time
            )
            
        except Exception as e:
            return SolutionResult(
                status=SolutionStatus.RUNTIME_ERROR,
                execution_time=time.time() - start_time,
                error_message=f"Unexpected error: {e}",
                traceback_info=traceback.format_exc()
            )
    
    def run_test_cases(self, problem_id: str) -> Dict[str, Any]:
        """Run all test cases for a problem"""
        if problem_id not in self.problems:
            return {"error": f"Problem {problem_id} not found"}
        
        problem = self.problems[problem_id]
        results = []
        
        for i, test_case in enumerate(problem.test_cases):
            print(f"Running test case {i + 1}: {test_case.description}")
            
            result = self.solve_problem(
                problem_id, 
                test_case.input_data, 
                test_case.time_limit
            )
            
            # Check if output matches expected
            if result.status == SolutionStatus.SUCCESS:
                if result.output.strip() == test_case.expected_output.strip():
                    result.status = SolutionStatus.SUCCESS
                    print(f"✓ Test case {i + 1}: PASSED")
                else:
                    result.status = SolutionStatus.WRONG_ANSWER
                    result.error_message = f"Expected: {test_case.expected_output.strip()}, Got: {result.output.strip()}"
                    print(f"✗ Test case {i + 1}: WRONG ANSWER")
            else:
                print(f"✗ Test case {i + 1}: {result.status.value}")
            
            results.append({
                "test_case": i + 1,
                "status": result.status.value,
                "execution_time": result.execution_time,
                "output": result.output,
                "expected": test_case.expected_output,
                "error": result.error_message
            })
        
        # Summary
        passed = sum(1 for r in results if r["status"] == "success")
        total = len(results)
        
        summary = {
            "problem_id": problem_id,
            "total_tests": total,
            "passed": passed,
            "failed": total - passed,
            "success_rate": passed / total if total > 0 else 0,
            "results": results
        }
        
        return summary

def demo_problem_solver():
    """Demonstrate the problem solver framework"""
    print("=== Olympic Problem Solver Demo ===")
    
    # Create solver
    solver = ProblemSolver()
    
    # Register problems
    sum_problem = SumProblem()
    palindrome_problem = PalindromeProblem()
    fibonacci_problem = FibonacciProblem()
    
    solver.register_problem(sum_problem)
    solver.register_problem(palindrome_problem)
    solver.register_problem(fibonacci_problem)
    
    # Add test cases for sum problem
    sum_problem.add_test_case(
        "3\n1 2 3",
        "6",
        description="Simple sum test"
    )
    sum_problem.add_test_case(
        "5\n-1 0 1 2 3",
        "5",
        description="Sum with negative numbers"
    )
    
    # Add test cases for palindrome problem
    palindrome_problem.add_test_case(
        "racecar",
        "YES",
        description="Simple palindrome"
    )
    palindrome_problem.add_test_case(
        "hello",
        "NO",
        description="Not a palindrome"
    )
    
    # Add test cases for fibonacci problem
    fibonacci_problem.add_test_case(
        "0",
        "0",
        description="Fibonacci(0)"
    )
    fibonacci_problem.add_test_case(
        "10",
        "55",
        description="Fibonacci(10)"
    )
    
    # Run test cases
    problems_to_test = ["SUM001", "STR001", "DP001"]
    
    for problem_id in problems_to_test:
        print(f"\n{'='*50}")
        print(f"Testing Problem: {problem_id}")
        print('='*50)
        
        summary = solver.run_test_cases(problem_id)
        
        print(f"\nSummary for {problem_id}:")
        print(f"  Total tests: {summary['total_tests']}")
        print(f"  Passed: {summary['passed']}")
        print(f"  Failed: {summary['failed']}")
        print(f"  Success rate: {summary['success_rate']:.1%}")
        
        # Show failed tests
        failed_tests = [r for r in summary['results'] if r['status'] != 'success']
        if failed_tests:
            print(f"  Failed tests:")
            for test in failed_tests:
                print(f"    Test {test['test_case']}: {test['status']} - {test['error']}")

def demo_error_handling():
    """Demonstrate error handling capabilities"""
    print("\n=== Error Handling Demo ===")
    
    solver = ProblemSolver()
    sum_problem = SumProblem()
    solver.register_problem(sum_problem)
    
    # Test various error conditions
    error_cases = [
        ("Invalid input format", "invalid\ninput"),
        ("Constraint violation", "1000000\n1 2 3"),  # n too large
        ("Missing input", "5"),  # Missing second line
        ("Wrong number count", "3\n1 2"),  # Only 2 numbers instead of 3
    ]
    
    for description, input_data in error_cases:
        print(f"\nTesting: {description}")
        result = solver.solve_problem("SUM001", input_data)
        print(f"Status: {result.status.value}")
        if result.error_message:
            print(f"Error: {result.error_message}")

# Test the framework
if __name__ == "__main__":
    demo_problem_solver()
    demo_error_handling()
    
    print("\n=== Bài tập thực hành ===")
    print("1. Extend framework với more problem types (Graph, Geometry)")
    print("2. Add memory usage monitoring")
    print("3. Implement parallel test execution")
    print("4. Build web interface cho problem submission")
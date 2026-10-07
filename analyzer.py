import ast
import tokenize

from rules import (
    check_undefined_variables,
    check_unused_variables,
    check_nested_loops,
    check_comparison_mistakes
)
from utils import read_file


class CodeAnalyzer:

    def __init__(self, file_path):
        self.file_path = file_path
        self.code = ""
        self.tree = None
        self.issues = []

    def analyze(self):
        self.code = read_file(self.file_path)

        # Check syntax
        try:
            self.tree = ast.parse(self.code, filename=self.file_path)
        except SyntaxError as error:
            self.issues.append({
                "type": "ERROR",
                "line": error.lineno,
                "message": error.msg
            })
            return

        # Run different checks
        self.issues.extend(
            check_undefined_variables(self.tree)
        )

        self.issues.extend(
            check_unused_variables(self.tree)
        )

        self.issues.extend(
            check_nested_loops(self.tree)
        )

        self.issues.extend(
            check_comparison_mistakes(self.code)
        )

    def display_results(self):
        print(f"\nFile: {self.file_path}")
        print("-" * 50)

        if not self.issues:
            print("✅ No major mistakes found!")
            print("Your code looks good.")
            return

        errors = 0
        warnings = 0
        suggestions = 0

        for issue in self.issues:

            issue_type = issue["type"]
            line = issue["line"]
            message = issue["message"]

            if issue_type == "ERROR":
                errors += 1

            elif issue_type == "WARNING":
                warnings += 1

            else:
                suggestions += 1

            print(f" {issue_type} - Line {line}")
            print(f"   {message}")
            print()

        print("-" * 50)
        print(f"Total Issues : {len(self.issues)}")
        print(f"Errors       : {errors}")
        print(f"Warnings     : {warnings}")
        print(f"Suggestions  : {suggestions}")
        print("-" * 50)
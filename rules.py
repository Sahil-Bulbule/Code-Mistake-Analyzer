import ast
import re


def check_undefined_variables(tree):
    issues = []

    defined_variables = set()

    # First collect variables
    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):
                    defined_variables.add(target.id)

        elif isinstance(node, ast.FunctionDef):
            for argument in node.args.args:
                defined_variables.add(argument.arg)

    # Check used variables
    for node in ast.walk(tree):

        if isinstance(node, ast.Name):

            if isinstance(node.ctx, ast.Load):

                if node.id not in defined_variables:

                    builtins = {
                        "print",
                        "len",
                        "range",
                        "str",
                        "int",
                        "float",
                        "list",
                        "dict",
                        "set",
                        "tuple",
                        "True",
                        "False",
                        "None"
                    }

                    if node.id not in builtins:
                        issues.append({
                            "type": "WARNING",
                            "line": node.lineno,
                            "message": (
                                f"Variable '{node.id}' may be undefined."
                            )
                        })

    return issues


def check_unused_variables(tree):
    issues = []

    assigned_variables = {}
    used_variables = set()

    for node in ast.walk(tree):

        if isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):
                    assigned_variables[target.id] = target.lineno

        elif isinstance(node, ast.Name):

            if isinstance(node.ctx, ast.Load):
                used_variables.add(node.id)

    for variable, line in assigned_variables.items():

        if variable not in used_variables:

            issues.append({
                "type": "WARNING",
                "line": line,
                "message": (
                    f"Variable '{variable}' is assigned "
                    f"but never used."
                )
            })

    return issues


def check_nested_loops(tree):
    issues = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.For, ast.While)):

            for child in ast.walk(node):

                if child is node:
                    continue

                if isinstance(child, (ast.For, ast.While)):

                    issues.append({
                        "type": "SUGGESTION",
                        "line": node.lineno,
                        "message": (
                            "Nested loop detected. "
                            "This may result in O(n²) time complexity."
                        )
                    })

                    break

    return issues


def check_comparison_mistakes(code):
    issues = []

    lines = code.splitlines()

    for line_number, line in enumerate(lines, start=1):

        stripped = line.strip()

        if (
            stripped.startswith("if ")
            or stripped.startswith("elif ")
            or stripped.startswith("while ")
        ):

            condition = stripped

            if re.search(r"\s=\s", condition):
                issues.append({
                    "type": "SUGGESTION",
                    "line": line_number,
                    "message": (
                        "Possible mistake: use '==' for comparison "
                        "instead of '='."
                    )
                })

    return issues
# CodeMistake Analyzer 🐍

CodeMistake Analyzer is a simple Python-based static code analysis tool
that checks Python source code for common programming mistakes and
provides useful suggestions.

The project is completely built using Python's standard library.

---

## 🚀 Features

- Detect Python syntax errors
- Detect potentially undefined variables
- Detect unused variables
- Detect nested loops
- Identify possible `=` vs `==` mistakes
- Display line numbers for detected issues
- Categorize issues into:
  - Errors
  - Warnings
  - Suggestions
- Command-line based interface

---

## 🛠️ Technologies Used

- Python
- AST (Abstract Syntax Tree)
- Regular Expressions
- File Handling
- Exception Handling
- Command Line Arguments

No external Python libraries are required.

---

## 📁 Project Structure

```text
CodeMistake-Analyzer/
│
├── main.py
├── analyzer.py
├── rules.py
├── utils.py
├── sample_code.py
├── sample_valid.py
├── requirements.txt
└── README.md


## Run :

python main.py sample_valid.py
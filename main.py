import sys
from analyzer import CodeAnalyzer


def main():
    print("=" * 50)
    print("           CODEMISTAKE ANALYZER")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage:")
        print("python main.py <python_file>")
        print("\nExample:")
        print("python main.py sample_code.py")
        return

    file_path = sys.argv[1]

    analyzer = CodeAnalyzer(file_path)
    analyzer.analyze()
    analyzer.display_results()


if __name__ == "__main__":
    main()
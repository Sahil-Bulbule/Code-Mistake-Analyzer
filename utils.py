def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"\nFile not found: {file_path}")
        exit()

    except PermissionError:
        print(f"\nPermission denied: {file_path}")
        exit()

    except Exception as error:
        print(f"\nError reading file: {error}")
        exit()
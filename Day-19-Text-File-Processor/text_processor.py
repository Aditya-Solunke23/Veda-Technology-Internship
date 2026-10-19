
print("========================================")
print("          TEXT FILE PROCESSOR")
print("========================================")

filename = input("\nEnter the text filename: ").strip()

if not filename:
    print("Error: Filename cannot be empty.")
else:
    try:
        line_count = 0
        word_count = 0
        character_count = 0

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_count += 1
                word_count += len(line.split())
                character_count += len(line)

        print("\n========== FILE STATISTICS ==========")
        print(f"Filename   : {filename}")
        print(f"Lines      : {line_count}")
        print(f"Words      : {word_count}")
        print(f"Characters : {character_count}")
        print("=====================================")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")

    except UnicodeDecodeError:
        print("Error: The file is not valid UTF-8 text.")

    except OSError as error:
        print(f"Error while reading the file: {error}")

import sys

def wc(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)
            char_count = sum(len(line) for line in lines)

        print(f"Lines: {line_count}")
        print(f"Words: {word_count}")
        print(f"Characters: {char_count}")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc_tool.py <file_path>")
    else:
        wc(sys.argv[1])
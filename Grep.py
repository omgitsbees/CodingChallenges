import os
import re
import argparse
import sys

def grep_file(pattern, filepath, ignore_case=False, invert_match=False):
    """
    Grep-like function to search for a pattern in a file.
    Supports case-insensitive search and inverted match.
    """
    flags = re.IGNORECASE if ignore_case else 0
    compiled_pattern = re.compile(pattern, flags)
    
    with open(filepath, 'r', encoding='utf-8') as file:  # Fixed the missing comma here
        for line in file:
            match = compiled_pattern.search(line)
            if match and not invert_match:
                print(f"{filepath}:{line.strip()}")
            elif not match and invert_match:
                print(f"{filepath}:{line.strip()}")


def grep_directory(pattern, directory, recursive=False, ignore_case=False, invert_match=False):
    """
    Search for a pattern in a directory recursively if needed.
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            grep_file(pattern, filepath, ignore_case, invert_match)
        if not recursive:
            break  # if not recursive, don't traverse subdirectories


def grep(pattern, paths, recursive=False, ignore_case=False, invert_match=False):
    """
    Main grep function. Supports multiple file inputs and directories.
    """
    for path in paths:
        if os.path.isfile(path):
            grep_file(pattern, path, ignore_case, invert_match)
        elif os.path.isdir(path):
            grep_directory(pattern, path, recursive, ignore_case, invert_match)


def main():
    """
    Main function to parse arguments and execute the grep functionality.
    """
    parser = argparse.ArgumentParser(description="A Python implementation of the grep tool.")
    parser.add_argument('pattern', help="The pattern to search for.")
    parser.add_argument('files', nargs='+', help="Files or directories to search in.")
    parser.add_argument('-r', '--recursive', action='store_true', help="Recursively search directories.")
    parser.add_argument('-v', '--invert', action='store_true', help="Invert match, exclude lines matching the pattern.")
    parser.add_argument('-i', '--ignore-case', action='store_true', help="Case insensitive search.")
    
    args = parser.parse_args()

    # If the pattern is empty, print all lines
    if args.pattern == "":
        for path in args.files:
            if os.path.isfile(path):
                with open(path, 'r', encoding='utf-8') as file:
                    sys.stdout.write(file.read())
            elif os.path.isdir(path):
                grep_directory("", path, recursive=args.recursive)
        return

    # Support for \d and \w in the pattern
    pattern = args.pattern
    pattern = pattern.replace("\\d", r"\d").replace("\\w", r"\w")

    # Execute grep with parsed arguments
    grep(pattern, args.files, recursive=args.recursive, ignore_case=args.ignore_case, invert_match=args.invert)


if __name__ == "__main__":
    main()

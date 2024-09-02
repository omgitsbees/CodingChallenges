import sys 
import argparse 

def cut(lines, fields, delimiter):
    if fields is None:
        return lines  # Return the full line if no fields are provided
    result = []
    fields = [int(f) - 1 for f in fields.split(',')]  # Convert fields to 0-indexed
    for line in lines:
        parts = line.strip().split(delimiter)
        try:
            selected = [parts[f] for f in fields if f < len(parts)]
            result.append(delimiter.join(selected))
        except IndexError:
            result.append('')  # Append empty if field is out of range
    return result

def main():
    parser = argparse.ArgumentParser(description="Perform a cut operation on input data.")
    parser.add_argument('-f', '--fields', required=True, help="Fields to extract (comma-separated).")
    parser.add_argument('-d', '--delimiter', default=' ', help="Delimiter (default is space).")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="Input file (default is stdin).")

    args = parser.parse_args()

    # Read input lines
    lines = args.file.readlines()

    # Perform cut operation
    output = cut(lines, args.fields, args.delimiter)

    # Output the result
    for line in output:
        print(line)

if __name__ == "__main__":
    main()
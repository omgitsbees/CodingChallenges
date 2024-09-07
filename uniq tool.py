import sys

def uniq_default(input_stream, output_stream):
    previous_line = None
    for line in input_stream:
        line = line.rstrip()  # Remove trailing newlines
        if line != previous_line:
            output_stream.write(line + '\n')
        previous_line = line

def uniq_count(input_stream, output_stream):
    previous_line = None
    count = 0
    for line in input_stream:
        line = line.rstrip()
        if line == previous_line:
            count += 1
        else:
            if previous_line is not None:
                output_stream.write(f"{count} {previous_line}\n")
            previous_line = line
            count = 1
    if previous_line is not None:
        output_stream.write(f"{count} {previous_line}\n")

def uniq_repeated(input_stream, output_stream):
    previous_line = None
    count = 0
    for line in input_stream:
        line = line.rstrip()
        if line == previous_line:
            count += 1
        else:
            if count > 1:
                output_stream.write(f"{previous_line}\n")
            previous_line = line
            count = 1
    if count > 1:
        output_stream.write(f"{previous_line}\n")

def uniq_unique(input_stream, output_stream):
    previous_line = None
    count = 0
    for line in input_stream:
        line = line.rstrip()
        if line == previous_line:
            count += 1
        else:
            if count == 1:
                output_stream.write(f"{previous_line}\n")
            previous_line = line
            count = 1
    if count == 1:
        output_stream.write(f"{previous_line}\n")

if __name__ == "__main__":
    # Determine input and output streams
    if len(sys.argv) < 2 or sys.argv[1] == '-':
        input_stream = sys.stdin
    else:
        try:
            input_stream = open(sys.argv[1], 'r')
        except FileNotFoundError:
            print(f"File {sys.argv[1]} not found.", file=sys.stderr)
            sys.exit(1)

    if len(sys.argv) < 3 or sys.argv[-1].startswith('-'):
        output_stream = sys.stdout
    else:
        output_stream = open(sys.argv[-1], 'w')

    # Detect options
    options = set(arg for arg in sys.argv[1:-1] if arg.startswith('-'))

    # Execute corresponding function based on options
    if '-d' in options and '-c' in options:
        uniq_count(input_stream, output_stream)
    elif '-d' in options:
        uniq_repeated(input_stream, output_stream)
    elif '-u' in options:
        uniq_unique(input_stream, output_stream)
    elif '-c' in options:
        uniq_count(input_stream, output_stream)
    else:
        uniq_default(input_stream, output_stream)

    # Close files if necessary
    if input_stream != sys.stdin:
        input_stream.close()
    if output_stream != sys.stdout:
        output_stream.close()
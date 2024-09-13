import sys
import argparse
if sys.platform != 'win32':
    import curses
else:
    try:
        import windows_curses as curses
    except ImportError:
        curses = None

# Step 1: Longest Common Subsequence (LCS) Algorithm
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Recover the LCS from the dp table
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_str))

# Step 2: Array (Line-by-Line) LCS
def lcs_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct LCS for lines
    i, j = m, n
    lcs_lines = []
    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            lcs_lines.append(arr1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return list(reversed(lcs_lines))

# Step 3: Generate diff between two arrays of lines
def diff_arrays(arr1, arr2):
    lcs_lines = lcs_arrays(arr1, arr2)
    diff = []
    i, j = 0, 0
    for line in lcs_lines:
        while i < len(arr1) and arr1[i] != line:
            diff.append(f"< {arr1[i]}")
            i += 1
        while j < len(arr2) and arr2[j] != line:
            diff.append(f"> {arr2[j]}")
            j += 1
        diff.append(f"  {line}")
        i += 1
        j += 1

    while i < len(arr1):
        diff.append(f"< {arr1[i]}")
        i += 1
    while j < len(arr2):
        diff.append(f"> {arr2[j]}")
        j += 1

    return diff

# Step 4: Optional Side-by-Side Diff Output
def side_by_side_diff(arr1, arr2):
    max_len = max(len(arr1), len(arr2))
    diff = []
    
    for i in range(max_len):
        line1 = arr1[i] if i < len(arr1) else ""
        line2 = arr2[i] if i < len(arr2) else ""
        diff.append(f"{line1:<50} | {line2}")
    
    return diff

# Step 5: GUI using curses for terminal-based visualization
def curses_diff(stdscr, file1_lines, file2_lines, diff_lines):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for i, line in enumerate(diff_lines):
        if i >= h - 1:  # Prevent overflow
            break
        stdscr.addstr(i, 0, line)

    stdscr.refresh()
    stdscr.getch()

# Helper function to load files into arrays of lines
def load_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()

# Step 6: Display diff based on user input
def display_diff(file1, file2, side_by_side=False, use_gui=False):
    lines1 = load_file(file1)
    lines2 = load_file(file2)

    if side_by_side:
        diffs = side_by_side_diff(lines1, lines2)
    else:
        diffs = diff_arrays(lines1, lines2)

    if use_gui and curses:
        curses.wrapper(curses_diff, lines1, lines2, diffs)
    else:
        print("\n".join(diffs))

# Command-line argument handling
def main():
    parser = argparse.ArgumentParser(description="Diff tool")
    parser.add_argument('file1', type=str, help="First file to compare")
    parser.add_argument('file2', type=str, help="Second file to compare")
    parser.add_argument('--side-by-side', action='store_true', help="Display diffs side by side")
    parser.add_argument('--gui', action='store_true', help="Display diffs using GUI")
    
    args = parser.parse_args()

    if args.gui and not curses:
        print("GUI not supported on Windows without 'windows-curses'.")
        sys.exit(1)

    display_diff(args.file1, args.file2, args.side_by_side, args.gui)

if __name__ == "__main__":
    main()

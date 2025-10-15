import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!
def match_digit(input_line):
    for char in input_line:
        if char.isdigit():
            return True
    return False
def match_word(input_line):
    for char in input_line:
        if char.isalpha() or char.isdigit() or char=="_":
            return True
    return False
def positive_ch_groups(input_line, pattern):
    chars = pattern[1:-1]
    for char in input_line:
        if char in chars:
            return True
    return False
def negative_ch_groups(input_line, pattern):
    chars = pattern[2:-1] #cat => [^abc]
    for char in input_line:
        if char not in chars:
            return True
    return False

def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == r"\d":
        return match_digit(input_line)
    elif pattern == r"\w":
       return match_word(input_line)
    elif pattern[0] == "[" and pattern[1]=="^" and pattern[-1] == "]":
        return negative_ch_groups(input_line,pattern)
    elif pattern[0] == "[" and pattern[-1] == "]":
        return positive_ch_groups(input_line,pattern)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()

import sys


def count_String(text):

    '''
    This program takes a string and count the total
    number of characters in the string:
    the number of upper cases.
    the number of  lower cases.
    the number of spaces.
    the number of punctuation marks 
    the number of digits and prints them in stdout.
    If no argument is provided, the user is prompted to enter a string manually.
    '''

    text_len = len(text)
    upper_count = 0
    lower_count = 0
    space_count = 0
    digit_count = 0
    punc_count = 0
    for c in text:
        if c.isupper():
            upper_count += 1
        elif c.islower():
            lower_count += 1
        elif c.isdigit():
            digit_count += 1
        elif c.isspace():
            space_count += 1
        elif not c.isalnum() and not c.isspace() and c != '\n':
            punc_count += 1
    print(f"The text contains {text_len} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punc_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def main():
        if len(sys.argv) < 2:
            print("What is the text to count")
            text = sys.stdin.readline()
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]
        count_String(text)


if __name__ == "__main__":
    try:
        print(count_String.__doc__)
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        sys.exit(0)

import sys

def main():
    try:
        if len(sys.argv) != 2 :
            raise AssertionError("Please provide exactly one argument")
        arg = sys.argv[1]
        try:
            number = int(arg)
        except ValueError:
            raise AssertionError("Please provide exactly number")
        match number % 2:
            case 0:
                print("I'm even")
            case _:
                print("I'm Odd")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
if __name__ == "__main__":
    main()
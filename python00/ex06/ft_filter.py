def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of
    iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def main():
    numbers = [0, 1, 2, 3, 4, 5]

    print("Original list:", numbers)

    even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
    print("Even numbers:", list(even_numbers))

    truthy_values = ft_filter(None, numbers)
    print("Truthy values:", list(truthy_values))


if __name__ == "__main__":
    print(main.__doc__)
    main()
    print(ft_filter.__doc__)

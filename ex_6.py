from math import sqrt


def find_dividers(numb: int) -> list:
    """
    Find all dividers of a given number.

    Args:
        numb: Integer to find divisors for

    Returns:
        List of sorted divisors
    """
    dividers = set()
    for n in range(1, int(sqrt(numb) + 1)):
        if numb % n == 0:
            dividers.add(n)
            dividers.add(numb // n)
    return sorted(list(dividers))


if __name__ == '__main__':
    numb = int(input('Enter the number: '))
    print(find_dividers(numb))

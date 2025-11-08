def generate_list(string: str) -> list:
    """
    Convert a string of space-separated numbers into a list of integers.

    Takes a string containing numbers separated by spaces, splits it into
    individual elements, and converts each element to an integer.

    Args:
        input_string (str): A string containing numbers separated by spaces

    Returns:
        list: A list of integers parsed from the input string
    """
    result = string.split()
    int_result = [int(item) for item in result]
    return int_result


if __name__ == '__main__':
    string = input('Enter numbers separated by spaces: ')
    numb_list = generate_list(string)
    print(sum(numb_list) / len(numb_list))

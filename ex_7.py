def generate_list(string: str) -> list:
    """
       Convert a string of space-separated numbers into a list of integers.

       Takes a string containing numbers separated by spaces, splits it into
       individual string elements, and converts each element to an integer.

       Args:
           string (str): A string containing numbers separated by spaces

       Returns:
           list: A list of integers parsed from the input string
       """
    numb_list = string.split()
    int_numb_list = [int(item) for item in numb_list]
    return int_numb_list


def sum_odd(numb_list: list) -> int:
    """
       Calculate the sum of all odd numbers in the given list.

       Args:
           numb_list (list): A list of integers

       Returns:
           int: The sum of all odd integers in the list
       """
    result = sum(
        [item for item in numb_list if item % 2 != 0]
    )
    return result


def sum_even(numb_list: list) -> int:
    """
        Calculate the sum of all even numbers in the given list.

        Args:
            numb_list (list): A list of integers

        Returns:
            int: The sum of all even integers in the list
        """
    result = sum(
        [item for item in numb_list if item % 2 == 0]
    )
    return result


if __name__ == '__main__':
    string = input('Enter numbers separated by spaces: ')
    numb_list = generate_list(string)
    print(sum_even(numb_list), sum_odd(numb_list))

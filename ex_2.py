def input_numbs() -> list:
    """
        Prompt the user to enter numbers separated by spaces.

        Returns:
            list: A list of strings representing the entered numbers.
        """
    numbers_string = input('Enter numbers separated by spaces')
    result = numbers_string.split()
    return result


def remove_three(old_list: list) -> list:
    """
        Remove the first occurrence of '3' from the input list.

        Args:
            old_list (list): The original list of string elements.

        Returns:
            list: A new list with the first '3' removed. Returns None if no '3' is found.
        """
    new_list = old_list.remove('3')
    return new_list


if __name__ == '__main__':
    original_list = input_numbs()
    print(remove_three(original_list))

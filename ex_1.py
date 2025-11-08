def input_numbs() -> list:
    """
    Prompt the user to enter 10 numbers one by one.

    Returns:
        list: A list of 10 integers entered by the user.
    """
    result = []
    for i in range(10):
        result.append(
            int(input(f'Enter the {i + 1} number'))
        )
    return result


def calculate_three_elements_sum(numb_list: list) -> list:
    """
       Calculate the sum of each consecutive three-element window in the list.

       For a list of 10 elements, this calculates 8 sums where each sum is
       the addition of elements at positions (i-1, i, i+1) for i from 1 to 8.

       Args:
           number_list (list): A list of numbers (must have at least 3 elements)

       Returns:
           list: A list of sums for each three-element window
       """
    result = []
    for ind in range(1, 9):
        result.append(
            numb_list[ind - 1] + numb_list[ind] + numb_list[ind + 1]
        )
    return result


if __name__ == '__main__':
    numb_list = input_numbs()
    print(calculate_three_elements_sum(numb_list))

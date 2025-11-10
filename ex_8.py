def sort_string(text: str) -> str:
    """
        Takes a string, sorts its characters, and returns the sorted string.

        Args:
            text (str): Source string to sort

        Returns:
            str: A string with characters sorted in alphabetical order
        """
    symbol_list = sorted(list(text))
    symbol_string = ''.join(symbol_list)
    return symbol_string


if __name__ == '__main__':
    text = input('Enter the text: ')
    print(sort_string(text))

def change_items(
        string1: str,
        string2: str,
        start: int,
        end: int
) -> None:
    """
        Transfer elements between two lists within a specified range.

        This function takes two strings, converts them to lists, and transfers elements
        from the first list to the second list within the specified start and end indices.
        The transfer happens in reverse order from end to start index.

        Args:
            string1 (str): First input string to be converted to a list
            string2 (str): Second input string to be converted to a list  
            start (int): Starting index for the range of elements to transfer
            end (int): Ending index for the range of elements to transfer

        Returns:
            None: This function prints the results rather than returning them
        """
    lst1 = string1.split()
    lst1_copied = lst1[:]
    lst2 = string2.split()

    for ind in range(end , start - 2, -1):
        lst2.append(lst1_copied[ind])
        lst1.remove(lst1[ind])

    print(f'1-st list: {lst1} \n2-nd list: {lst2}')


if __name__ == '__main__':
    string1 = input('Enter the 1-st string: ')
    string2 = input('Enter the 2-nd string: ')
    start, end = (map(
        int, input('Enter the range separated by spaces: ').split())
    )

    change_items(
        string1,
        string2,
        start, end
    )

def list_shift(string: str, command: str) -> list:
    """
      Perform a cyclic shift on a list of elements based on a given command.

      This function takes a space-separated string of elements and a shift command,
      then returns a new list with elements cyclically shifted according to the command.

      Args:
          string (str): Space-separated elements to be shifted
          command (str): Shift command in format 'R#' or 'L#' where # is the number of positions

      Returns:
          list: A new list with elements shifted according to the command
      """
    lst = string.split()
    shift = int(command[1])
    if command[0].lower() == 'r':
        result = lst[shift - 1:] + lst[:shift - 1]
    if command[0].lower() == 'l':
        result = lst[shift:] + lst[:shift]
    return result


if __name__ == '__main__':
    string = input('Enter elements of list: ')
    command = input('Enter the command: ')
    print(list_shift(string, command))

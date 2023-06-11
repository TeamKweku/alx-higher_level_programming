#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ function that finds all multiples of 2
        Args:
            my_list: list of ints

        Returns:
            new_list
    """
    if not my_list:
        return
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return (new_list)

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """ Function that deletes an item at a
        position in a list

        Args:
            my_list: provided list
            idx: index to delete item

        Returns:
            modified list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    del my_list[idx]

    return (my_list)

#!/usr/bin/python3
def weight_average(my_list=[]):
    """ Function that returns the weighted average of
        all integers tuple

        Args:
            my_list: provided list of tuple

        Returns:
            weighted average
    """
    if not my_list:
        return (0)
    mul = 0
    denom = 0
    for tup in my_list:
        mul += (tup[0] * tup[1])
        denom += tup[1]
    weight_average = mul / denom

    return (weight_average)

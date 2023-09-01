#!/usr/bin/python3
"""Model of this task"""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers

    Args:
    list_of_integers (list): A list of unsorted integers.

    Returns:
        int or None: The peak element if found, otherwise None.

    Note:
        This algorithm uses a bianry search approach to find the peak element.
        Time Complexity: O(log(n)), where n is the number of
                        elements in the list.
    """
    size = len(list_of_integers)

    if size == 0:
        return None

    if size == 1:
        return list_of_integers[0]

    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    left = list_of_integers[mid - 1]
    right = list_of_integers[mid + 1]
    if peak > left and peak > right:
        return peak
    elif peak < left:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

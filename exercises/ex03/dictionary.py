"""Exercise 03 - Dictionary Functions"""

__author__ = "730567850"


def invert(not_inv: dict[str, str]) -> dict[str, str]:
    """Invert keys and values"""
    result = {}
    for key in not_inv:
        value = not_inv[key]
        if value in result:
            raise KeyError("Duplicate value identified")
        result[value] = key
    return result


def count(cnt_lst: list[str]) -> dict[str, int]:
    """Count number of times value appears in list"""
    result = {}
    for current in cnt_lst:
        if current in result:
            result[current] += 1
        else:
            result[current] = 1
    return result


def favorite_color(names_colors: dict[str, str]) -> str:
    """Return the most frequently occurring color"""
    color_count = {}

    for key in names_colors:
        color = names_colors[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    frequent_color = None
    highest_count = 0

    for color in color_count:
        count = color_count[color]
        if count > highest_count:
            frequent_color = color
            highest_count = count
        elif count == highest count and frequent_color is None:
            frequent_color = color
    return frequent_color

def bin_len(bins: list[str]) -> dict[int, set[str]]:
    """Turn list of strings into a dictionary"""
    result = {}

    for item in bins:
        length = len(item)

        if length in result:
            result[length].add(item)
        else:
            result[length] = {item}

    return result

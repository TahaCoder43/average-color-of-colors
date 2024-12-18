from typing import List, Tuple
from functools import reduce

COLOR_PROMPT = "Enter a valid color, or enter anything else to stop and get result (Valid color is hexadecimal format and accounts for the alpha):"
EXIT_PROMPT = "Do you want to get the average (Y/n):"
COLOR_ADDED_SUCCESS_PROMPT = "Added!!"
REMIND_TO_ADD_VALID_COLOR = "ENTER A VALID COLOR THEN!!!"


def validate_color(color: str):
    return color.startswith("#") and (len(color) == 7 or len(color) == 9)


"""Only accepts a single hex letters and maps it to a decimal digit"""


def map_hex_digit(hex_digit: str) -> int:
    hex_digit = hex_digit.lower()

    if len(hex_digit) != 1:
        raise TypeError("map_hex_digit only accepts a single digit")

    if hex_digit not in "1234567890abcdef":
        raise TypeError("Invalid hex, hex digit should be from 1234567890abcdef")

    if hex_digit in "1234567890":
        return int(hex_digit)

    match hex_digit:
        case "a":
            return 10
        case "b":
            return 11
        case "c":
            return 12
        case "d":
            return 13
        case "e":
            return 14
        case "f":
            return 15

    raise AssertionError("Program should not reach here")


def hex_to_dec(hex: str) -> int:
    if len(hex) != 2:
        raise TypeError("hex_to_dec only accepts 2 digit hex")

    dec = map_hex_digit(hex[0]) * 16 + map_hex_digit(hex[1]) * 1
    return dec


def format_colors(color: str) -> Tuple[int, int, int, int]:
    if not __name__ == "__main__":
        if not validate_color(color):
            raise TypeError("Provide a valid color with #AAAAAA or #AAAAAAAA format")

    if len(color) == 7:
        color = color + "ff"
    hex_color = color.strip("#")

    rgba = tuple(hex_to_dec(hex_color[i : i + 2]) for i in range(0, 8, 2))

    if len(rgba) != 4:
        raise TypeError("Tuple should be of length 4")

    return rgba


def find_average(colors: List[str]) -> Tuple[float, float, float, float]:
    formatted_colors = map(format_colors, colors)
    total_color = reduce(
        lambda total, color: tuple(total[i] + color[i] for i in range(4)),
        formatted_colors,
    )
    average_color = tuple(
        one_of_rgba_total_value / len(colors) for one_of_rgba_total_value in total_color
    )

    if len(average_color) != 4:
        raise TypeError("average_color should be a tuple of length 4")
    return average_color


def main():
    colors: List[str] = []
    color = input(COLOR_PROMPT)
    if not validate_color(color):
        return

    while validate_color(color):
        colors.append(color)
        print(COLOR_ADDED_SUCCESS_PROMPT)
        color = input(COLOR_PROMPT)
        while not validate_color(color):
            exit_input = input(EXIT_PROMPT)
            if exit_input == "n":
                print(REMIND_TO_ADD_VALID_COLOR)
                color = input(COLOR_PROMPT)
            else:
                break

    average_color = find_average(colors)

    print(average_color)


if __name__ == "__main__":
    main()

#!/usr/bin/python3

"""
Log Parsing
"""

import sys


def print_stats(total_size, status_codes):
    """
    Print the computed statistics.

    Args:
        total_size (int): The total file size.
        status_codes (dict): A dictionary with status codes as keys
            and their counts as values.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) == 9:
                ip, date, path, status, size = (
                    parts[0],
                    parts[3],
                    parts[6],
                    parts[7],
                    parts[8],
                )

                if status in status_codes:
                    status_codes[status] += 1

                total_size += int(size)
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        pass

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

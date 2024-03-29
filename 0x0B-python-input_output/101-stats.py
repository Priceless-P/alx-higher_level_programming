#!/usr/bin/python3
# 101-stats.py
# Brennan D Baraban <375@holbertonschool.com>
"""Reads from standard input and computes metrics.

After every ten each_lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size_ up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size_, status_code):
    """Print accumulated metrics.
    Args:
        size_: Accumulated read file size_.
        status_code: Accumulated count of status codes.
    """
    print("File size_: {}".format(size_))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))

if __name__ == "__main__":
    import sys

    size_ = 0
    status_code = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for each_line in sys.stdin:
            if count == 10:
                print_stats(size_, status_code)
                count = 1
            else:
                count += 1

            each_line = each_line.split()

            try:
                size_ += int(each_line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if each_line[-2] in valid_codes:
                    if status_code.get(each_line[-2], -1) == -1:
                        status_code[each_line[-2]] = 1
                    else:
                        status_code[each_line[-2]] += 1
            except IndexError:
                pass

        print_stats(size_, status_code)

    except KeyboardInterrupt:
        print_stats(size_, status_code)
        raise

#!/usr/bin/python3
import sys

lines_count = 0
total_file_size = 0
status_codes = {}

try:
    for line in sys.stdin:
        lines_count += 1

    # Extract file size and status cpde from line
    _, _, _, _, status_code, file_size = line.split()

    # Update total file size
    total_file_size += int(file_size)

    # Update status code count
    status_codes[status_code] = status_codes.get(status_code, 0)

    if lines_count % 10 == 0:
        print("File size: {}".format(total_file_size))
        for code in sorted(status_codes.keys()):
            print("{}: {}".format(code, status_codes[code]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))

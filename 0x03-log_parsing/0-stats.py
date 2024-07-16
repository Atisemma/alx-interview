#!/usr/bin/python3
import sys
import re
from collections import defaultdict


def print_stats(total_size, status_codes):
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code]:
            print(f"{code}: {status_codes[code]}")


def parse_line(line):
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    match = re.match(pattern, line)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None, None


def main():
    total_size = 0
    status_codes = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status, size = parse_line(line.strip())

            if status and size:
                total_size += size
                status_codes[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

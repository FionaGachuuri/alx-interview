#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
After every 10 lines and/or a keyboard interruption
(CTRL + C), print these statistics:
    - Total file size: File size: <total size>
    - Number of lines by status code:
        - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
        - format: <status code>: <number>
        - status codes should be printed in ascending order
"""

import sys
import re


def print_stats(total_size, status_codes):
    """
    Print the statistics.

    Args:
        total_size (int): The total file size.
        status_codes (dict): The count of each status code.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """
    Main function to process stdin line by line and compute metrics.
    """
    # Initialize variables
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    # Define the pattern to match the log format
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\]
    "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)

            if match:
                _, _, status_code, file_size = match.groups()
  
                try:
                    status_code = int(status_code)
                    file_size = int(file_size)

                    # Update metrics
                    total_size += file_size
                    if status_code in status_codes:
                        status_codes[status_code] += 1
                except ValueError:
                    # Skip if status_code or file_size is not a valid integer
                    pass

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
     
    except KeyboardInterrupt:
        # Handle Ctrl+C interruption
        pass
    finally:
        # Print the final stats
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

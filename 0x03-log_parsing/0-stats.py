#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import signal

def print_statistics(total_size, status_code_counts):
    print(f"Total file size: {total_size}")
    for code in sorted(status_code_counts):
        print(f"{code}: {status_code_counts[code]}")

def main():
    total_size = 0
    status_code_counts = {}

    try:
        lines_processed = 0

        for line in sys.stdin:
            # Parse the line
            parts = line.split()
            if len(parts) != 10 or parts[5] != '"GET' or not parts[8].isdigit():
                # Skip invalid lines
                continue

            file_size = int(parts[8])
            status_code = int(parts[9])

            # Update metrics
            total_size += file_size
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            lines_processed += 1

            if lines_processed % 10 == 0:
                print_statistics(total_size, status_code_counts)

    except KeyboardInterrupt:
        # Handle CTRL+C
        print_statistics(total_size, status_code_counts)
        sys.exit(0)

if _name_ == "_main_":
    main()
#!/usr/bin/python3
import sys
if __name__ == '__main__':
    total_sum = 0
    argv_len = len(sys.argv) - 1
    if (argv_len > 0):
        for num in range(1, argv_len + 1):
            total_sum += int(sys.argv[num])
    print('{:d}'.format(total_sum))

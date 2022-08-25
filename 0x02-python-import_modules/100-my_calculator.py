#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv_len = len(sys.argv) - 1
    if (not argv_len == 3):
        print('Usage: ', end='')
        for idx in range(0, len(sys.argv)):
            print('{}'.format(sys.argv[idx]), end=" ")

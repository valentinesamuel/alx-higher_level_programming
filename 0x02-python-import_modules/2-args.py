#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv_len = len(sys.argv) - 1
    if (argv_len == 0):
        print('{:d} arguments.'.format(argv_len))
    elif (argv_len == 1):
        print('{:d} argument:'.format(argv_len))
        print('{:d}: {:s}'.format(argv_len ,sys.argv[1]))
    elif (argv_len > 1):
        print('{:d} arguments:'.format(argv_len))
        for idx in range(1, argv_len + 1):
            print('{:d}: {:s}'.format(idx, sys.argv[idx]))

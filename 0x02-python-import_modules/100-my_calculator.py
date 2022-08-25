#!/usr/bin/python3
import sys
import calculator_1 as calc
if __name__ == '__main__':
    argv_len = len(sys.argv) - 1
    ops = {'+', '+', '-', '/'}
    if (not argv_len == 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if not sys.argv[2] in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    if operator == '+':
        result = calc.add(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    elif operator == '-':
        result = calc.sub(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    elif operator == '*':
        result = calc.mul(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    elif operator == '/':
        result = calc.div(a, b)
        print('{} {} {} = {}'.format(a, operator, b, result))
    print('')

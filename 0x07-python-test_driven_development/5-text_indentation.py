#!/usr/bin/python3
"""
    text_indentation: print 2 newlines instead of every period,
        question mark, or colon character.
"""


def text_indentation(text):
    """
    print 2 newlines instead of every period,
        question mark, or colon character.
    Args:
        text (str): string of text to format
    """
    if text is None or type(text) is not str:
        raise TypeError("text must be a string")

    isSkip = False
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i, '\n' * 2, end="", sep="")
            isSkip = True
        else:
            if i == ' ' and isSkip:
                continue
            else:
                print(i, end="", sep="")
                isSkip = False

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")

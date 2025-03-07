"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import examplepackagefb1258.wisdom as wisdom


def main():
    """
    Get some wise text and print it out.
    """
    line = wisdom.get()  # get a line of text
    print(line)  # print it out


if __name__ == "__main__":
    # run the main function
    main()

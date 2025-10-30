"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

from pyfortunecookie.core import get_fortune, get_lucky_number, get_color

def main():
    print("🥠 Welcome to PyFortune Cookie!\n")
    print(f"Today's fortune: {get_fortune()}")
    print(f"Your lucky number: {get_lucky_number()}")
    print(f"Your lucky color: {get_color()}")

if __name__ == "__main__":
    main()

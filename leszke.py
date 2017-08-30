import sys
from random import randint


def main(argv):
    if len(argv) < 2:
        count = randint(1, 100)
        print("D" + (count - 1) * "d")
    else:
        try:
            count = int(argv[1]);
            print("D" + (count - 1) * "d")
        except ValueError:
            print("Jak pan śmie! Czeba liczbem podać!")


if __name__ == "__main__":
    main(sys.argv)

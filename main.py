import math


def is_rectangle(a, b, c):
    """
    Check if three given points form a rectangle by checking if any two sides
    satisfy Pythagoras' theorem (a^2 + b^2 = c^2)
    :param a: tuple (x, y)
    :param b: tuple (x, y)
    :param c: tuple (x, y)
    :return: bool (True if a rectangle can be formed, else False.)
    """
    ab = distance(a, b)
    bc = distance(b, c)
    ac = distance(a, c)
    return ab == math.sqrt(bc**2 + ac**2) or bc == math.sqrt(ab**2 + ac**2) or ac == math.sqrt(ab**2 + bc**2)


def distance(point1, point2):
    """
    Calculate the distance between two points.
    :param point1: tuple (x, y)
    :param point2: tuple (x, y)
    :return: float (Distance between the two points.)
    """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def is_inside_rectangle(a, b, c, x):
    """
    Check if "x" is inside a rectangle formed by "abc".
    :param a: tuple (x, y)
    :param b: tuple (x, y)
    :param c: tuple (x, y)
    :param x: tuple (x, y)
    :return: bool (True if the point is inside the rectangle, else False.)
    """
    return min(a[0], b[0], c[0]) < x[0] < max(a[0], b[0], c[0]) and min(a[1], b[1], c[1]) < x[1] < max(a[1], b[1], c[1])


def diagonal_length(a, b, c):
    """
    Calculate diagonal length of "abc" rectangle.
    :param a: tuple (x, y)
    :param b: tuple (x, y)
    :param c: tuple (x, y)
    :return: float
    """
    ab = distance(a, b)
    bc = distance(b, c)
    ac = distance(a, c)
    return max(ab, bc, ac)


def main():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            a = tuple(map(float, lines[0].strip().split(',')))
            b = tuple(map(float, lines[1].strip().split(',')))
            c = tuple(map(float, lines[2].strip().split(',')))
            x = tuple(map(float, lines[3].strip().split(',')))

    except FileNotFoundError:
        print("File not found! Please make sure to include file type extension (example: rectangle.txt")
    except ValueError:
        print("Error: Invalid value in the file.")

    print(f"Rectangle can be formed: {is_rectangle(a, b, c)}")
    print(f"X is inside rectangle: {is_inside_rectangle(a, b, c, x)}")
    print(f"Diagonal length of the rectangle: {diagonal_length(a, b, c)}")


if __name__ == "__main__":
    main()

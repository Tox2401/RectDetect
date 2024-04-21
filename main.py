import math


def is_rectangle(points):
    """
    Check if the given points form a rectangle in n-dimensional space.
    :param points: list of tuples representing the coordinates of points
    :return: bool, True if a rectangle can be formed, else False
    """
    num_points = len(points)
    # Calculate distances between all pairs of points
    distances = [[distance(points[i], points[j]) for j in range(num_points)] for i in range(num_points)]
    print(distances)

    # Check if any pair of distances satisfy the conditions for forming a rectangle
    for i in range(num_points):
        for j in range(i + 1, num_points):
            for k in range(j + 1, num_points):
                # Check if any two sides satisfy the Pythagorean theorem
                sides = sorted([distances[i][j], distances[j][k], distances[i][k]])
                if round(sum(side ** 2 for side in sides[:-1]), 8) == round(sides[-1] ** 2, 8):
                    return True
    return False


def distance(point1, point2):
    """
    Calculate the distance between two points.
    :param point1: tuple representing the coordinates of point 1
    :param point2: tuple representing the coordinates of point 2
    :return: float, the distance between the two points
    """
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


def is_inside_rectangle(points, x):
    """
    Check if a point x is inside a rectangle formed by the given points.
    :param points: list of tuples representing the coordinates of points
    :param x: tuple representing the coordinates of point x
    :return: bool (True if the point is inside the rectangle, else False.)
    """
    min_coords = [min(p[i] for p in points) for i in range(len(points[0]))]
    max_coords = [max(p[i] for p in points) for i in range(len(points[0]))]
    return all(min_coord <= xi <= max_coord for min_coord, max_coord, xi in zip(min_coords, max_coords, x))


def diagonal_length(points):
    """
    Calculate the diagonal length of the rectangle formed by the given points.
    :param points: list of tuples representing the coordinates of points
    :return: float, the diagonal length of the rectangle
    """
    min_coords = [min(p[i] for p in points) for i in range(len(points[0]))]
    max_coords = [max(p[i] for p in points) for i in range(len(points[0]))]
    squared_sum = sum((max_coord - min_coord) ** 2 for min_coord, max_coord in zip(min_coords, max_coords))
    return math.sqrt(squared_sum)


def main():
    file_name = input("Enter the file name: ")

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            points = [tuple(map(float, line.strip().split(','))) for line in lines[:-1]]
            x = tuple(map(float, lines[-1].strip().split(',')))
            dimensions = len(points[0])

    except FileNotFoundError:
        print("File not found! Please make sure to include file type extension (example: rectangle.txt")
        return
    except ValueError:
        print("Error: Invalid value in the file.")
        return

    if len(points) < 2:
        print("Insufficient points to form a rectangle.")
        return
    elif is_rectangle(points):
        match dimensions:
            case 2:
                print("Type: Rectangle (2D)")
            case 3:
                print("Type: Cuboid (3D)")
            case _:
                print(f"Type: {dimensions}D Hyperrectangle")
        print(f"X is inside rectangle: {is_inside_rectangle(points, x)}")
        print(f"Diagonal length of the rectangle: {diagonal_length(points)}")
    else:
        print("Type: Not a rectangle")


if __name__ == "__main__":
    main()

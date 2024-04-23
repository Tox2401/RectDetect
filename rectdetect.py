import math


def is_rectangle(vertices):
    """
    Check if the given points form a rectangle in n-dimensional space.
    :param vertices: list of tuples representing the coordinates of points
    :return: bool, int, True if a rectangle can be formed, and number of dimensions
    """
    dimensions = len(vertices[0])
    dimensional_values = [[] for _ in range(dimensions)]

    for point in vertices:
        for i in range(dimensions):
            dimensional_values[i].append(point[i])

    for dimensional_value in dimensional_values:
        if len(set(dimensional_value)) != 2:
            if len(set(dimensional_value)) == 1:
                dimensions -= 1
                continue
            return False

    return True, dimensions


def distance(vertex1, vertex2):
    """
    Calculate the distance between two points.
    :param vertex1: tuple representing the coordinates of point 1
    :param vertex2: tuple representing the coordinates of point 2
    :return: float, the distance between the two points
    """
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(vertex1, vertex2)))


def is_inside_rectangle(vertices, x):
    """
    Check if a point x is inside or on the edge of a rectangle formed by the given points.
    :param vertices: list of tuples representing the coordinates of points
    :param x: tuple representing the coordinates of point x
    :return: bool (True if the point is inside the rectangle, else False.)
    """
    min_coords = [min(p[i] for p in vertices) for i in range(len(vertices[0]))]
    max_coords = [max(p[i] for p in vertices) for i in range(len(vertices[0]))]
    return all(min_coord <= xi <= max_coord for min_coord, max_coord, xi in zip(min_coords, max_coords, x))


def diagonal_length(vertices):
    """
    Calculate the diagonal length of the rectangle formed by the given points.
    :param vertices: list of tuples representing the coordinates of points
    :return: float, the diagonal length of the rectangle
    """
    min_coords = [min(p[i] for p in vertices) for i in range(len(vertices[0]))]
    max_coords = [max(p[i] for p in vertices) for i in range(len(vertices[0]))]
    squared_sum = sum((max_coord - min_coord) ** 2 for min_coord, max_coord in zip(min_coords, max_coords))
    return round(math.sqrt(squared_sum), 4)


def main():
    while True:
        file_name = input("Enter the file name: ")

        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                vertices = [tuple(map(float, line.strip().split(','))) for line in lines[:-1]]
                x = tuple(map(float, lines[-1].strip().split(',')))
                rectangle, dimensions = is_rectangle(vertices)

        except FileNotFoundError:
            print("File not found! Please make sure to include file type extension (example: rectangle.txt)")
            continue
        except ValueError:
            print("Error: Invalid value in the file.")
            continue

        if len(vertices) < 3:
            print("Insufficient vertices to form a rectangle.")
            return
        elif rectangle:
            match dimensions:
                case _ if dimensions <= 0:
                    print("Type: Dot (0D)")
                    return
                case 1:
                    print("Type: Line (1D)")
                    return
                case 2:
                    print("Type: Rectangle (2D)")
                case 3:
                    print("Type: Cuboid (3D)")
                case _:
                    print(f"Type: {dimensions}D Hyperrectangle")
            print(f"X is inside: {is_inside_rectangle(vertices, x)}")
            print(f"Diagonal length: {diagonal_length(vertices)}")
        else:
            print("Vertices provided cannot form a rectangle.")

        choice = input("Press Enter to exit or enter 'yes' to process another file: ").lower()
        if choice != 'yes':
            break


if __name__ == "__main__":
    main()

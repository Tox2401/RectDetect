# 1.0 Basic RectDetect

This Python script analyzes three points to determine if they can form a rectangle in 2D space. It checks if any two sides of the triangle formed by the points satisfy Pythagoras' theorem. Additionally, it checks if a given point is inside or on the edge of the rectangle and calculates the diagonal length of the rectangle.

# 2.0 RectDetect

This Python script analyzes a set of points to determine if they form a rectangle in n-dimensional space. It also provides additional information such as the type of shape formed, whether a point is inside or on the edge of the rectangle, and the diagonal length of the rectangle.

## 2.1 Features

- Checks if the given points form a rectangle in n-dimensional space.
- Determines the type of shape formed by the points (e.g., Dot, Line, Rectangle, Cuboid, Hyperrectangle).
- Checks if a point is inside or on the edge of the rectangle.
- Calculates the diagonal length of the rectangle.

## 2.2 How to Use

1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Navigate to the directory where the program is located.
4. Prepare a text file containing the coordinates of the points. Each line should represent a point, with coordinates separated by commas. The last line should contain the coordinates of the point to be checked against the rectangle.
5. Run the program by executing the following command in your terminal:

    ```
    python rectdetect.py
    ```

6. Follow the on-screen prompts to enter the file name containing the coordinates.
7. The program will display the type of shape formed, whether the point is inside the rectangle, and the diagonal length of the rectangle.

**Note:** If there are fewer points provided than required to form a complete rectangle, the program will assume the missing points based on the provided ones, as long as the provided points satisfy the conditions of forming a rectangle.

## 2.3 Example Input File (rectangle.txt provided)

0, 0, 0  
5, 0, 0  
0, 3, 0  
0, 0, 1  
1, 1, 2  

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or find any issues, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

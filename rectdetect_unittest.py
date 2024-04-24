import unittest
from rectdetect import is_rectangle, is_inside_rectangle, diagonal_length


class TestRectangleFunctions(unittest.TestCase):
    def test_is_rectangle(self):
        # Test case where points form a 2D rectangle
        points_2d = [(0, 0), (0, 2), (3, 0), (3, 2)]
        self.assertTrue(is_rectangle(points_2d)[0])
        self.assertEqual(is_rectangle(points_2d)[1], 2)

        # Test case where points form a 3D rectangle (cuboid)
        points_3d = [(0, 0, 0), (0, 2, 0), (3, 0, 0), (3, 2, 0), (0, 0, 3), (0, 2, 3), (3, 0, 3), (3, 2, 3)]
        self.assertTrue(is_rectangle(points_3d)[0])
        self.assertEqual(is_rectangle(points_3d)[1], 3)

        # Test case where points do not form a rectangle
        points_2d_not_rectangle = [(0, 0), (1, 1), (2, 2), (3, 3)]
        self.assertFalse(is_rectangle(points_2d_not_rectangle)[0])
        self.assertEqual(is_rectangle(points_2d_not_rectangle)[1], 2)

        # Test case where points do not form a 3D rectangle (cuboid)
        points_3d_not_rectangle = [(0, 0, 0), (0, 2, 0), (3, 0, 0), (3, 2, 0), (0, 0, 3), (0, 2, 3), (3, 0, 3), (4, 2, 3)]
        self.assertFalse(is_rectangle(points_3d_not_rectangle)[0])
        self.assertEqual(is_rectangle(points_3d_not_rectangle)[1], 3)

        # Test case where 3 dimensions are provided, but 3rd dimension is empty
        points_3d = [(0, 0, 0), (0, 2, 0), (3, 0, 0), (3, 2, 0), (0, 0, 0), (0, 2, 0), (3, 0, 0), (3, 2, 0)]
        self.assertTrue(is_rectangle(points_3d)[0])
        self.assertEqual(is_rectangle(points_3d)[1], 2)

    def test_is_inside_rectangle(self):
        # Test case where point x is inside the 2D rectangle
        points_2d = [(0, 0), (0, 2), (3, 0), (3, 2)]
        x_inside_2d = (1, 1)
        self.assertTrue(is_inside_rectangle(points_2d, x_inside_2d))

        # Test case where point x is outside the 2D rectangle
        x_outside_2d = (4, 4)
        self.assertFalse(is_inside_rectangle(points_2d, x_outside_2d))

        # Test case where point x is inside the 3D rectangle (cuboid)
        points_3d = [(0, 0, 0), (0, 2, 0), (3, 0, 0), (3, 2, 0), (0, 0, 3), (0, 2, 3), (3, 0, 3), (3, 2, 3)]
        x_inside_3d = (1, 1, 1)
        self.assertTrue(is_inside_rectangle(points_3d, x_inside_3d))

        # Test case where point x is outside the 3D rectangle (cuboid)
        x_outside_3d = (4, 4, 4)
        self.assertFalse(is_inside_rectangle(points_3d, x_outside_3d))

    def test_diagonal_length(self):
        # Test case for diagonal length calculation of 2D rectangle
        points_2d = [(0, 0), (0, 2), (3, 0), (3, 2)]
        expected_length_2d = 3.6056
        self.assertAlmostEqual(diagonal_length(points_2d), expected_length_2d, delta=0.0001)

        # Test case for diagonal length calculation of 3D rectangle (cuboid)
        points_3d = [(0, 0, 0), (0, 2, 0), (3, 0, 0), (3, 2, 0), (0, 0, 3), (0, 2, 3), (3, 0, 3), (3, 2, 3)]
        expected_length_3d = 4.6904
        self.assertAlmostEqual(diagonal_length(points_3d), expected_length_3d, delta=0.0001)


if __name__ == '__main__':
    unittest.main()

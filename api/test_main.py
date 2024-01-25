# test_main.py
import unittest
from main import find_vertices
import numpy as np


class TestImageProcessing(unittest.TestCase):
    def test_find_vertices(self):
        # Create a sample image for testing
        img = 255 * np.ones((100, 100, 3), dtype=np.uint8)
        img[20:80, 20:80, :] = 0

        vertices = find_vertices(img)

        self.assertEqual(len(vertices), 1)
        self.assertEqual(len(vertices[0]["coordinates"]), 4)

    def test_find_vertices_blank_image(self):
        # Create a sample image for testing
        img = 255 * np.ones((100, 100, 3), dtype=np.uint8)

        vertices = find_vertices(img)

        self.assertEqual(len(vertices), 0)


if __name__ == "__main__":
    unittest.main()

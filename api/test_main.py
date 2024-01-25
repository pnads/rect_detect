"""Unit tests for api/main.py using pytest"""
import numpy as np
from fastapi.testclient import TestClient
from pathlib import Path
from main import app, find_vertices

client = TestClient(app)


def test_extract_rect_coords():
    img_path = Path(__file__).parent.parent / "images" / "simple.png"
    with open(img_path, "rb") as image_file:
        response = client.post(
            "extract-rect-coords", files={"file": (image_file.name, image_file)}
        )
    assert response.status_code == 200
    assert response.json() == [
        {"id": 0, "coordinates": [[387, 55], [437, 56], [436, 456], [386, 455]]},
        {"id": 1, "coordinates": [[231, 55], [281, 56], [280, 456], [230, 455]]},
        {"id": 2, "coordinates": [[75, 55], [125, 56], [124, 456], [74, 455]]},
    ]


def test_find_vertices():
    # Create a sample image for testing
    img = 255 * np.ones((100, 100, 3), dtype=np.uint8)
    img[20:80, 20:80, :] = 0

    vertices = find_vertices(img)

    assert len(vertices) == 1
    assert len(vertices[0]["coordinates"]) == 4


def test_find_vertices_blank_image():
    # Create a sample image for testing
    img = 255 * np.ones((100, 100, 3), dtype=np.uint8)

    vertices = find_vertices(img)

    assert len(vertices) == 0

"""
This module provides an endpoint for extracting the coordinates of rectangle vertices in an image file.
It uses FastAPI to serve the endpoint and OpenCV for image processing.

To run locally with auto-reload: `uvicorn main:app --reload`

Author: Patrick Nadeau
"""
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import numpy as np
from numpy import uint8
from numpy.typing import NDArray
import cv2

app = FastAPI()


def find_vertices(image_array: NDArray[uint8]) -> list[dict]:
    """
    Processes the input image and extracts the coordinates of rectangle vertices.

    Args:
    - image_array: numpy.ndarray, input image in BGR format

    Returns:
    - list of dictionaries, each containing the 'id' and 'coordinates' of rectangle vertices
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(gray, 127, 255, 0)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    count = 0
    vertices = []
    for contour in contours:
        # Find the approximate contour for each of the contours
        approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)

        if is_rectangle(approx) and not is_bounding_box(image_array, contour):
            corners = np.intp(approx)
            corner_dict = {"id": count, "coordinates": corners.reshape(4, 2).tolist()}
            vertices.append(corner_dict)
            count += 1
    return vertices


def is_rectangle(approx_contour):
    """Utility function to check if an approximate contour has 4 vertices."""
    return len(approx_contour) == 4


def is_bounding_box(image, contour):
    """Utility function to check if the input contour is actually the bounding box for the image,
    so it can be excluded."""
    image_perimeter = (image.shape[0] + image.shape[1] - 2) * 2
    contour_perimeter = cv2.arcLength(contour, True)
    return int(image_perimeter) == int(contour_perimeter)


@app.post("/extract-rect-coords")
async def extract_rect_coords(file: UploadFile = File(...)):
    """
    Extracts the coordinates of rectangle vertices in the input image.

    Args:
    - file: UploadFile, the input image file

    Returns:
    - JSONResponse: JSON response containing the coordinates of rectangle vertices in the input image
    """
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    vertices = find_vertices(img)
    return JSONResponse(content=vertices)

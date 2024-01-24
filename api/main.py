from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
from fastapi.responses import JSONResponse

app = FastAPI()


def extract_rect_coords(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    ret, thresh = cv2.threshold(gray, 127, 255, 0)

    # Find contours in the binary image
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    )

    # Loop over all contours
    count = 0
    corner_list = []
    for i, cnt in enumerate(contours):
        # Find the approximate contour for each of the contours
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4 and hierarchy[0, i, -1] != -1:
            # If the number of vertex points in the approximate contour is 4, it's a rectangle
            corners = np.intp(approx)
            corner_dict = {"id": count, "coordinates": corners.reshape(4, 2).tolist()}
            corner_list.append(corner_dict)
            count += 1
    return corner_list


@app.post("/extract-rect-coords")
async def extract_rect_coordinates(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    corner_coordinates = extract_rect_coords(img)
    return JSONResponse(content=corner_coordinates)

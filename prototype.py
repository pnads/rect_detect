
import numpy as np
import cv2



def extract_rect_coords(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    ret, thresh = cv2.threshold(gray, 127, 255, 0)

    # Find contours in the binary image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over all contours
    count = 0
    corner_list = []
    for i, cnt in enumerate(contours):
        # Find the approximate contour for each of the contours
        approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4 and hierarchy[0,i,-1] != -1:
            # If the number of vertex points in the approximate contour is 4, it's a rectangle
            # x, y, w, h = cv2.boundingRect(cnt)
            # Draw the rectangle
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Get the coordinates of the corners
            corners = np.intp(approx)
            # corner_dict[str(count)] = corners
            corner_dict = {
                "id": count,
                "coordinates": corners.reshape(4,2).tolist()
            }
            corner_list.append(corner_dict)
            count += 1
            # for corner in corners:
            #     x, y = corner.ravel()
            #     cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    return corner_list

if __name__ == "__main__":
    image = cv2.imread("images/simple.png")
    corners = extract_rect_coords(image)
    print(corners)

    image = cv2.imread("images/rotated.png")
    corners = extract_rect_coords(image)
    print(corners)
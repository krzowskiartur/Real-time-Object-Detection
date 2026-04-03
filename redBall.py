import cv2
import numpy as np
import os


def getCenterPoint(contours):
    bestArea = 0
    bestCenterPoint = [0, 0]

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > bestArea:
            bestArea = area
            x, y, w, h = cv2.boundingRect(contour)
            bestCenterPoint = [int(x + (w / 2)), int(y + (h / 2))]

    return bestCenterPoint


def main():
    cap = cv2.VideoCapture(r'mwa/sawmovie.mp4')
    #print(os.path.exists('mwa/sawmovie.mp4'))
    success, frame = cap.read()
    scale = 0.4

    while success:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, np.array([0, 80, 100]), np.array([10, 255, 255]))

        window = np.ones((10, 10), np.uint8)
        mask = cv2.dilate(mask, window)

        window = np.ones((3, 3), np.uint8)
        mask = cv2.erode(mask, window)

        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        c = getCenterPoint(contours)

        cv2.line(frame, (c[0], c[1] - 50), (c[0], c[1] + 50), (255, 0, 0), 3)
        cv2.line(frame, (c[0] - 50, c[1]), (c[0] + 50, c[1]), (255, 0, 0), 3)

        cv2.imshow("Moving ball", cv2.resize(frame, (int(frame.shape[1] * scale), int(frame.shape[0] * scale))))

        success, frame = cap.read()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

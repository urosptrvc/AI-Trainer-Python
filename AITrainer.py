import cv2
import numpy as np
import time
import PoseModule as pm

# Otvaranje kamere
cap = cv2.VideoCapture(0)

detector = pm.poseDetector()
count_right = 0
count_left = 0
dir_right = 0
dir_left = 0
pTime = 0

screen_width = 1920
screen_height = 1080

while True:
    success, img = cap.read()
    if not success:
        break

    # Skaliranje slike na fullscreen
    img = cv2.resize(img, (screen_width, screen_height))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        # Detekcija za desnu ruku
        angle_right = detector.findAngle(img, 12, 14, 16)
        per_right = np.interp(angle_right, (210, 310), (0, 100))
        bar_right = np.interp(angle_right, (210, 310), (650, 100))

        color_right = (255, 0, 255)
        if per_right == 100:
            color_right = (0, 255, 0)
            if dir_right == 0:
                count_right += 0.5
                dir_right = 1
        if per_right == 0:
            color_right = (0, 255, 0)
            if dir_right == 1:
                count_right += 0.5
                dir_right = 0

        # Detekcija za levu ruku
        angle_left = detector.findAngle(img, 11, 13, 15)
        per_left = np.interp(angle_left, (210, 310), (0, 100))
        bar_left = np.interp(angle_left, (210, 310), (650, 100))

        color_left = (255, 0, 255)
        if per_left == 100:
            color_left = (0, 255, 0)
            if dir_left == 0:
                count_left += 0.5
                dir_left = 1
        if per_left == 0:
            color_left = (0, 255, 0)
            if dir_left == 1:
                count_left += 0.5
                dir_left = 0

        # Prikaz bara i procenta za desnu ruku
        cv2.rectangle(img, (1800, 100), (1875, 650), color_right, 3)
        cv2.rectangle(img, (1800, int(bar_right)), (1875, 650), color_right, cv2.FILLED)
        cv2.putText(img, f'{int(per_right)}%', (1780, 75), cv2.FONT_HERSHEY_PLAIN, 3, color_right, 4)

        # Prikaz bara i procenta za levu ruku
        cv2.rectangle(img, (50, 100), (125, 650), color_left, 3)
        cv2.rectangle(img, (50, int(bar_left)), (125, 650), color_left, cv2.FILLED)
        cv2.putText(img, f'{int(per_left)}%', (30, 75), cv2.FONT_HERSHEY_PLAIN, 3, color_left, 4)

        # Prikaz broja ponavljanja za desnu ruku
        cv2.putText(img, f'Right: {int(count_right)}', (1570, 150), cv2.FONT_HERSHEY_PLAIN, 3, (51, 153, 255), 5)

        # Prikaz broja ponavljanja za levu ruku
        cv2.putText(img, f'Left: {int(count_left)}', (150, 150), cv2.FONT_HERSHEY_PLAIN, 3, (51, 153, 255), 5)

    cv2.namedWindow("Fitness Tracker", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Fitness Tracker", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Fitness Tracker", img)
    # Prikaz slike
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

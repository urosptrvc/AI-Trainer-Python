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

while True:
    success, img = cap.read()
    if not success:
        break

    # Rezolucija slike
    img = cv2.resize(img, (1280, 720))
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
        cv2.rectangle(img, (1100, 100), (1175, 650), color_right, 3)
        cv2.rectangle(img, (1100, int(bar_right)), (1175, 650), color_right, cv2.FILLED)
        cv2.putText(img, f'{int(per_right)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, color_right, 4)

        # Prikaz bara i procenta za levu ruku
        cv2.rectangle(img, (50, 100), (125, 650), color_left, 3)
        cv2.rectangle(img, (50, int(bar_left)), (125, 650), color_left, cv2.FILLED)
        cv2.putText(img, f'{int(per_left)} %', (50, 75), cv2.FONT_HERSHEY_PLAIN, 4, color_left, 4)

        # Prikaz broja ponavljanja za desnu ruku
        cv2.putText(img, f'Right: {int(count_right)}', (900, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

        # Prikaz broja ponavljanja za levu ruku
        cv2.putText(img, f'Left: {int(count_left)}', (50, 100), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 5)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Prikaz slike
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

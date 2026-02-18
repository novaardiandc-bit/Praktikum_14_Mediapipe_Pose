import cv2
import mediapipe as mp

mpose = mp.solutions.pose
pose = mpose.Pose()
mdraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgRGB)

    if hasil.pose_landmarks :
        mdraw.draw_landmarks (img, hasil.pose_landmarks, mpose.POSE_CONNECTIONS)

        landmarks = hasil.pose_landmarks.landmark

        right_shoulder = landmarks[mpose.PoseLandmark.RIGHT_SHOULDER.value]
        right_wrist = landmarks[mpose.PoseLandmark.RIGHT_WRIST.value]

        left_shoulder = landmarks[mpose.PoseLandmark.LEFT_SHOULDER.value]
        left_wrist = landmarks[mpose.PoseLandmark.LEFT_WRIST.value]

        if right_wrist.y < left_shoulder.y:
            cv2.putText(img, "Tangan Kanan Terangkat",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

        if left_wrist.y < left_shoulder.y:
            cv2.putText(img, "Tangan Kiri Terangkat",
                        (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

    cv2.imshow("webcam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




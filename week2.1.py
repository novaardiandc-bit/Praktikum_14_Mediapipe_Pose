import cv2
import mediapipe as mp

mpose = mp.solutions.pose #inisiasi mediapipe pos
pose = mpose.Pose()

cap = cv2.VideoCapture(0) # vidio dari webcam

while True:
    success, img = cap.read() #pembacaan image
    if not success:
        print ("kamera tidak terbaca")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    hasil = pose.process(imgRGB)
    if hasil.pose_landmarks:
        print ("terdeteksi")
    else:
        print ("tidak terdeteksi")

    cv2.imshow("webcam",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
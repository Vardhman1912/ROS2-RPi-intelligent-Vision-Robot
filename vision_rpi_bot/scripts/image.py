import cv2

# Open default camera (index 0)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

ret, frame = cap.read()
if not ret:
    print("❌ Failed to grab frame")
else:
    cv2.imwrite("opencv_test.jpg", frame)
    print("✅ Image saved as opencv_test.jpg")

cap.release()
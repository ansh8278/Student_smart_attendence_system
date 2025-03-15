import cv2
import numpy as np
import face_recognition
import os
from attendance import markAttendance

# Load the known face encodings
path = "faces"
images = []
classNames = []

imageList = os.listdir(path)

for imgName in imageList:
    if imgName.startswith("."):  # Ignore hidden system files like .DS_Store
        continue
    
    imgPath = os.path.join(path, imgName)
    img = cv2.imread(imgPath)
    
    if img is None:  # Skip if image reading fails
        print(f"❌ Error: Could not read image {imgPath}")
        continue

    images.append(img)
    classNames.append(os.path.splitext(imgName)[0])

# Encode known faces
knownEncodings = []
for img in images:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encodes = face_recognition.face_encodings(img)
    if encodes:
        knownEncodings.append(encodes[0])

print(f"✅ Encoding Complete! Encoded {len(knownEncodings)} faces.")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        print("❌ Error: Could not read frame from webcam.")
        continue  # Skip processing if frame is not captured

    imgS = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)  # Reduce image size
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(knownEncodings, encodeFace)
        faceDis = face_recognition.face_distance(knownEncodings, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Mark attendance
            markAttendance(name)

    cv2.imshow("Attendance System", img)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

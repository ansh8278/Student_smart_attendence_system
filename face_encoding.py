import cv2
import face_recognition
import numpy as np
import os

# Path to the folder containing images
path = "faces"
images = []
classNames = []

# Get all files in the directory
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
    classNames.append(os.path.splitext(imgName)[0])  # Extract name

# Function to encode known faces
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if encode:
            encodeList.append(encode[0])
    return encodeList

knownEncodings = findEncodings(images)
print(f"✅ Encoding Complete! Encoded {len(knownEncodings)} faces.")

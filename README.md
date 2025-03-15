Face Recognition Attendance System
📌 Introduction
Welcome to the Face Recognition Attendance System! This project leverages the power of face recognition technology to automatically detect faces from a live webcam feed and mark attendance in a CSV file. By utilizing libraries like OpenCV, face_recognition, and pandas, this system simplifies the attendance process, making it efficient and user-friendly.

🛠️ Installation
To get started, make sure you have Python installed on your computer. Then, you can easily install the necessary libraries by running the following command in your terminal:


pip install opencv-python numpy face-recognition pandas
📂 Project Structure
Here's a quick overview of the project structure:

Run
Copy code
FaceRecognition-Attendance
│── faces                  # Folder containing images of known faces
│── attendance.csv         # CSV file where attendance is recorded
│── attendance.py          # Function to mark attendance
│── face_recognition.py    # Main face recognition script
│── README.md              # Project documentation
📝 How It Works
Load Known Faces: The system starts by loading images of known individuals from the faces directory.
Encode Faces: It then encodes these known faces using the face_recognition library.
Real-Time Detection: The webcam is activated to detect faces in real-time.
Face Comparison: Detected faces are compared with the known encodings.
Mark Attendance: If a match is found, the system records the attendance in attendance.csv.
Continuous Operation: The system runs continuously until you decide to exit by pressing 'q'.



🚀 Running the Project
Step 1: Prepare Images
To begin, add images of the individuals whose attendance you want to track into the faces directory. Make sure the image files are named in the format PersonName.jpg (for example, JohnDoe.jpg).


Step 2: Run the Face Recognition Script
Once your images are ready, you can run the face recognition script by executing:

python face_recognition.py



Step 3: View Attendance
After running the script, attendance records will be saved in attendance.csv, which will include the following columns:

Name: The name of the recognized individual
Date: The date of attendance
Time: The time of attendance

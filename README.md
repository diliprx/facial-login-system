# 🔐 Facial Recognition Login System

A secure facial recognition-based login system built using Python, OpenCV, and Flask. 
This project allows users to register and log in using their face as biometric authentication, ensuring a modern and contactless access control method.

## 📌 Features

- User registration with facial capture
- Login authentication using real-time facial recognition
- SQLite database for storing user credentials and encodings
- Simple and user-friendly web interface (HTML + CSS + Flask)
- Local storage and validation using face encodings

---

## 🛠️ Setup Instructions

Follow the steps below to run this project locally:

### 1. Clone the Repository

bash:
git clone https://github.com/yourusername/facial-login-system.git
cd facial-login-system
### 2. Create Virtual Environment (Optional but Recommended)

python -m venv venv
venv\Scripts\activate   # On Windows
### 3. Install Required Dependencies

pip install -r requirements.txt
If you don't have requirements.txt, manually install:


pip install flask opencv-python face-recognition numpy
⚠️ Make sure you're using Python 3.12. If you face issues with face-recognition, install cmake first:


pip install cmake
pip install dlib
pip install face-recognition
### 4. Run the App

python app.py
Then open your browser and go to:
http://127.0.0.1:5000/

🗃️ Folder Structure
face-login/ 
├── app.py
├── database.db
├── static/
│   └── style.css
├── templates/
│   ├── login.html
│   └── register.html
└── README.md
🧠 How It Works
On register, the system captures your face from webcam and stores the encoding in the database.

On login, it compares the captured face with stored encodings using face-recognition.

If a match is found, the login is successful.

📌 Real-Life Importance
Facial recognition systems are widely used in:

Banking & Financial security

Airports and Border security

Smart home access systems

Corporate logins for sensitive systems

📧 Contact
Dilip Kumar V
B.E. Cyber Security Student
📧 dilipvenkat2006@gmail.com
📸 Instagram: @dilip__rx
💻 GitHub: @diliprx


from flask import Flask, render_template, request, redirect, flash
import face_recognition
import cv2
import numpy as np
import os, pickle, bcrypt
import sqlite3

app = Flask(__name__)
app.secret_key = 'securekey123'

# Setup DB
def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS users (email TEXT PRIMARY KEY, password TEXT)')
init_db()

ENCODINGS_PATH = 'face_data/encodings.pkl'
if not os.path.exists('face_data'):
    os.makedirs('face_data')
if not os.path.exists(ENCODINGS_PATH):
    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump({}, f)

# Helper: Load/Save Face Encodings
def load_encodings():
    with open(ENCODINGS_PATH, 'rb') as f:
        return pickle.load(f)

def save_encodings(encodings):
    with open(ENCODINGS_PATH, 'wb') as f:
        pickle.dump(encodings, f)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = bcrypt.hashpw(request.form['password'].encode(), bcrypt.gensalt())

        # Capture image
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cv2.imwrite("user.jpg", frame)
        cam.release()

        # Encode face
        img = face_recognition.load_image_file("user.jpg")
        encodings = face_recognition.face_encodings(img)

        if len(encodings) == 0:
            flash("No face detected!")
            return redirect('/register')

        # Save to DB
        with sqlite3.connect("database.db") as conn:
            conn.execute('INSERT OR REPLACE INTO users (email, password) VALUES (?, ?)', (email, password))

        # Save encoding
        known_encodings = load_encodings()
        known_encodings[email] = encodings[0]
        save_encodings(known_encodings)

        flash("Registration successful!")
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect("database.db") as conn:
            cur = conn.cursor()
            cur.execute('SELECT password FROM users WHERE email=?', (email,))
            data = cur.fetchone()
            if not data or not bcrypt.checkpw(password.encode(), data[0]):
                flash("Invalid credentials")
                return redirect('/login')

        # Capture image
        cam = cv2.VideoCapture(0)
        ret, frame = cam.read()
        cv2.imwrite("login.jpg", frame)
        cam.release()

        # Face match
        img = face_recognition.load_image_file("login.jpg")
        enc = face_recognition.face_encodings(img)

        if not enc:
            flash("No face detected!")
            return redirect('/login')

        known = load_encodings()
        result = face_recognition.compare_faces([known.get(email)], enc[0])

        if result[0]:
            flash("Login successful!")
        else:
            flash("Face does not match.")

        return redirect('/login')
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

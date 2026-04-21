# 🧠 Face & Hand Gesture Recognition System

A real-time computer vision project that detects **face landmarks and hand gestures** using **MediaPipe** and **OpenCV**.
The system can count fingers, identify basic gestures, and analyze facial features like mouth movement.

---

## 🚀 Features

* ✋ Hand Landmark Detection (Left & Right)
* 🔢 Finger Counting (Per hand + Total)
* 🤌 Basic Gesture Recognition (Fist, Open Hand, etc.)
* 😊 Face Landmark Detection
* 👄 Mouth Open Detection
* 📷 Real-time Webcam Support
* 🖼 Image & 🎥 Video input support (Streamlit UI)

---

## 🛠 Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy
* Streamlit (for UI)

---

## 📁 Project Structure

```
face-hand-landmarks/
│
├── app.py                # Streamlit web app (image/video)
├── main.py               # Webcam real-time detection
├── config.py             # Config settings
│
├── modules/
│   ├── detector.py       # Mediapipe detection logic
│   ├── drawer.py         # Drawing landmarks
│   ├── utils.py          # Helper functions
│
├── features/
│   ├── hand_gestures.py  # Finger counting & gestures
│   ├── face_features.py  # Face-based features
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gesture-recognition-app.git
cd gesture-recognition-app
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

### 🔹 Option 1: Real-Time Webcam (Best Demo)

```bash
python main.py
```

👉 This will:

* Open your webcam
* Detect face + hands
* Show finger count and gestures in real-time

---

### 🔹 Option 2: Streamlit Web App (Image/Video)

```bash
streamlit run app.py
```

👉 This will:

* Open a web interface
* Upload image/video
* Show detection results

---

## 🎯 Example Output

* Right Hand: 5
* Left Hand: 2
* Total Fingers: 7
* Gesture: Open Hand
* Mouth Open: True

---

## 🚧 Future Improvements

* 🔥 Train ML model for advanced gesture recognition
* 🎮 Control system (volume, games, apps) using gestures
* 🌐 Deploy full real-time app using WebRTC
* 📊 Add gesture history tracking

---

## 🙌 Acknowledgements

* MediaPipe by Google
* OpenCV community

---

## 📌 Note

* Webcam version works best locally
* Streamlit cloud deployment may not support real-time camera

---

## 📬 Contact

Feel free to connect or suggest improvements!

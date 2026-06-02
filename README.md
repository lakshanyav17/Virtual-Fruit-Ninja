# Virtual-Fruit-Ninja

A gesture-controlled virtual Fruit Ninja game that allows users to slice fruits using real-time hand movements captured through a webcam — no physical controller required.

---

## Overview

Virtual Fruit Ninja is an interactive computer vision–based game developed using OpenCV and MediaPipe.

The system detects hand gestures through a webcam and tracks the index finger movement to simulate a sword. When the user performs a fast slicing motion over a virtual fruit, the fruit is cut and the score increases.

This project demonstrates the practical application of computer vision, gesture recognition, and human–computer interaction (HCI).

---

## Demo
<img width="1600" height="1466" alt="output" src="https://github.com/user-attachments/assets/1b6e0ba8-063e-43ed-a6da-93274563fd36" />

---

## Features
 
1.No keyboard or mouse required.

2.Real-time hand gesture detection via webcam.

3.Physics-based fruit movement with gravity.

4.Live score tracking on screen.

5.Works on Windows, Linux, and macOS.

---

## Requirements

- Hardware.
- Webcam (inbuilt or external).
- Minimum 4 GB RAM.
- Processor: Intel i3 or higher.

---

## Software

- Python 3.8 – 3.11
- OpenCV
- MediaPipe
- NumPy

---

## Installation

```bash
# Clone the repository
git clone https://github.com/lakshanyav17/virtual-fruit-ninja.git
cd virtual-fruit-ninja

# Install dependencies
pip install numpy==1.26.4 opencv-python==4.9.0.80 mediapipe==0.10.9 protobuf==3.20.3
```

---

## How to Run

```bash
python fruitninja.py
Press Esc to quit the game.
```


## How It Works

```
1. Start webcam
        ↓
2. Detect hand landmarks using MediaPipe
        ↓
3. Track index finger tip movement
        ↓
4. Move fruit upward using gravity physics
        ↓
5. Detect slicing collision (finger speed + distance)
        ↓
6. Update score and respawn fruit
        ↓
7. Display output on screen
```

---

## Project Structure

```
virtual-fruit-ninja/
│
├── fruitninja.py        # Main game script
├── results/
│   ├── output1.png      # Sample output screenshots
│   └── output2.png
└── README.md
```

---

## Advantages

No external hardware needed beyond a webcam.

Real-time interaction with low latency.

Simple and beginner-friendly implementation.

Clearly demonstrates computer vision concepts.


## Limitations

Requires good lighting conditions for accurate detection.

Accuracy depends on webcam quality.

Single-player only.

Limited to index finger gesture.


## Future Scope

Add multiple fruits appearing simultaneously.

Add lives system and game over screen.

Support multiple gesture types (full hand slice).

Add sound effects on fruit slice.

Deploy as a web app using Streamlit or Flask.


## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| OpenCV | Webcam capture and image rendering |
| MediaPipe | Hand landmark detection |
| NumPy | Mathematical calculations (distance, speed) |

---


 ## Contact
 
**Lakshanya V** — lakshanyav17@gmail.com

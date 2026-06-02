import cv2
import mediapipe as mp
import numpy as np
import random

# Camera
cap = cv2.VideoCapture(0)

# Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Screen
W, H = 640, 480

# Fruit
fruit_x = random.randint(100, W - 100)
fruit_y = H
fruit_radius = 30
fruit_speed = -15
gravity = 1

# Score
score = 0

# Sword tracking
prev_x, prev_y = None, None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (W, H))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lm = hand.landmark[8]  # Index finger tip
            cx, cy = int(lm.x * W), int(lm.y * H)

            if prev_x is not None:
                # Draw sword
                cv2.line(frame, (prev_x, prev_y), (cx, cy), (255, 0, 0), 5)

                # Speed of finger
                speed = np.sqrt((cx - prev_x)**2 + (cy - prev_y)**2)

                # Collision only if fast movement
                dist = np.sqrt((cx - fruit_x)**2 + (cy - fruit_y)**2)
                if dist < fruit_radius and speed > 25:
                    score += 1
                    fruit_x = random.randint(100, W - 100)
                    fruit_y = H
                    fruit_speed = -15

            prev_x, prev_y = cx, cy
            mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
    else:
        prev_x, prev_y = None, None

    # Fruit physics
    fruit_y += fruit_speed
    fruit_speed += gravity

    if fruit_y > H:
        fruit_x = random.randint(100, W - 100)
        fruit_y = H
        fruit_speed = -15

    # Draw fruit
    cv2.circle(frame, (fruit_x, int(fruit_y)), fruit_radius, (0, 0, 255), -1)

    # Score
    cv2.putText(frame, f"Score: {score}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Virtual Fruit Ninja", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

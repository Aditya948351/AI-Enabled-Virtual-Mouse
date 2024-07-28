import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import pyttsx3
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize hand tracking
hands = mp_hands.Hands(max_num_hands=1)

# Initialize screen dimensions (adjust as needed)
screen_width, screen_height = pyautogui.size()

# Initialize camera screen dimensions for 720p resolution
camera_width, camera_height = 1280, 720

# Mouse movement speed factor
speed_factor = 2  # Adjust this value to change the speed

# Flags for hand gestures
left_click_gesture = False
right_click_gesture = False
scroll_gesture = False
mouse_movement_gesture = False
double_click_gesture = False
last_click_time = 0

# Flag for virtual mouse control
virtual_mouse_on = True  # Assume virtual mouse is already turned on

# Capture video from webcam
cap = cv2.VideoCapture(0)

# Speaks a message to indicate that the script will continue running until a key is pressed
engine = pyttsx3.init()
text = "Press Esc key to exit the program."
engine.say(text)
engine.runAndWait()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the image horizontally for a selfie-view
    display_image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(display_image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    if results.multi_hand_landmarks and virtual_mouse_on:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the image
            mp_drawing.draw_landmarks(display_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the positions of all fingers and wrist
            finger_coords = np.array([[l.x * camera_width, l.y * camera_height] for l in hand_landmarks.landmark])
            wrist_coords = np.array([hand_landmarks.landmark[0].x * camera_width, hand_landmarks.landmark[0].y * camera_height])

            # Detect thumb movement for mouse pointer control
            thumb_coords = finger_coords[4]
            if thumb_coords[0] < wrist_coords[0] - 50:  # Adjust the threshold for thumb movement
                mouse_movement_gesture = True
            else:
                mouse_movement_gesture = False

            # Detect left-click gesture (raise middle finger when index finger is raised)
            if finger_coords[8][1] < finger_coords[6][1] and finger_coords[12][1] > finger_coords[10][1]:
                left_click_gesture = True
            else:
                left_click_gesture = False

            # Detect right-click gesture (touch index finger to thumb and keep other fingers extended)
            if np.linalg.norm(finger_coords[4] - finger_coords[8]) < 40 \
                    and all(np.linalg.norm(finger_coords[i] - wrist_coords) > 40 for i in range(1, 5)):
                right_click_gesture = True
            else:
                right_click_gesture = False

            # Detect double-click gesture (touch index finger to middle finger)
            if np.linalg.norm(finger_coords[8] - finger_coords[12]) < 40:
                if time.time() - last_click_time < 0.3:
                    double_click_gesture = True
                last_click_time = time.time()
            else:
                double_click_gesture = False

            # Detect scroll gesture (lean ring finger downwards)
            if finger_coords[16][1] > finger_coords[14][1]:
                scroll_gesture = True
            else:
                scroll_gesture = False

            # Draw circles on finger tips
            index_finger_tip = tuple(np.array([finger_coords[8][0], finger_coords[8][1]]).astype(int))
            middle_finger_tip = tuple(np.array([finger_coords[12][0], finger_coords[12][1]]).astype(int))
            thumb_tip = tuple(np.array([finger_coords[4][0], finger_coords[4][1]]).astype(int))
            ring_finger_tip = tuple(np.array([finger_coords[16][0], finger_coords[16][1]]).astype(int))

            # Draw circles on the image
            cv2.circle(display_image, index_finger_tip, 10, (255, 0, 0), -1)  # Blue color
            cv2.circle(display_image, middle_finger_tip, 10, (255, 0, 0), -1)  # Blue color
            cv2.circle(display_image, thumb_tip, 10, (255, 192, 203), -1)  # Pink color
            cv2.circle(display_image, ring_finger_tip, 10, (0, 255, 0), -1)  # Green color

            # Perform actions based on gestures
            if left_click_gesture:
                pyautogui.click()

            if right_click_gesture:
                pyautogui.click(button='right')

            if double_click_gesture:
                pyautogui.doubleClick()

            if scroll_gesture:
                pyautogui.scroll(10)  # Scroll down

            if mouse_movement_gesture:
                new_x = max(0, min(thumb_coords[0] * speed_factor, screen_width - 1))
                new_y = max(0, min(thumb_coords[1] * speed_factor, screen_height - 1))
                pyautogui.moveTo(new_x, new_y)

    # Display the image with hand landmarks
    cv2.imshow('Virtual Mouse', display_image)

    if cv2.waitKey(1) & 0xFF == 27:  # Exit if 'Esc' key is pressed
        break

# Release resources
cap.release()
cv2.destroyAllWindows()



Virtual Mouse Control with Hand Gestures
This Python script enables virtual mouse control using hand gestures detected from a webcam feed. It utilizes OpenCV, Mediapipe, and PyAutoGUI libraries for hand tracking, gesture recognition, and mouse control.
Features
•	Hand Gesture Recognition: Detects various hand gestures such as left-click, right-click, double-click, scroll, and mouse movement.
•	Visual Feedback: Displays circles on fingertips to provide visual feedback for detected gestures.
•	Customizable Settings: Adjustable parameters for mouse movement speed, gesture thresholds, and screen dimensions.
•	User Interaction: Provides a user-friendly interface for controlling the virtual mouse through hand gestures.
Setup
1.	Install the required Python libraries:
Copy code and install following libraries using
          pip install opencv-python mediapipe pyautogui
pyautogui==0.9.53
opencv-python==4.5.3.56
mediapipe==0.8.6.2
2.	Ensure your webcam is connected and accessible.
3.	Run the script VirtualMouseWithHandGestures.py.
4.	Perform hand gestures in front of the webcam to control the virtual mouse.
Usage
•	Left-Click Gesture: Raise your middle finger while the index finger is raised.
•	Right-Click Gesture: Touch the index finger to the thumb and extend other fingers.
•	Double-Click Gesture: Touch the index finger to the middle finger quickly.
•	Scroll Gesture: Lean the ring finger downwards.
•	Mouse Movement Gesture: Move your thumb to control the mouse pointer.
Dependencies
•	OpenCV
•	Mediapipe
•	PyAutoGUI
•	NumPy
Notes
Adjust parameters like speed_factor, gesture thresholds, and screen dimensions in the script as needed.
•	Ensure proper lighting and hand visibility for accurate gesture detection.
•	Use a clear background and avoid cluttered environments for better performance.

Whats New!
1.We have added an protection such that it asks for users name and the password which is as follows:
              Name: Aditya
              Password: 123 
NOTE: this will not run unless you put this code and password
              After providing this name and password just click on the Start Virtual Mouse

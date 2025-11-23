import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
 
# Start Webcam
cap = cv2.VideoCapture(1)

# Helper Function: Determine if finger is up
def finger_up(hand_landmarks, finger_tip, finger_dip):
    return hand_landmarks.landmark[finger_tip].y < hand_landmarks.landmark[finger_dip].y

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip and convert color
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect gestures
            finger_states = {
                "thumb": finger_up(hand_landmarks, 4, 3),
                "index": finger_up(hand_landmarks, 8, 6),
                "middle": finger_up(hand_landmarks, 12, 10),
                "ring": finger_up(hand_landmarks, 16, 14),
                "pinky": finger_up(hand_landmarks, 20, 18)
            }

            # Example gestures
            if finger_states["index"] and not any([finger_states["middle"], finger_states["ring"], finger_states["pinky"]]):
                cv2.putText(frame, "MOVE FORWARD", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                pyautogui.keyDown('w')
            else:
                pyautogui.keyUp('w')

            if finger_states["index"] and finger_states["middle"]:
                cv2.putText(frame, "SHOOT", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                pyautogui.click()  # Simulate left mouse click

            if all(finger_states.values()):
                cv2.putText(frame, "JUMP", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                pyautogui.press('space')  # Jump key

    # Display frame
    cv2.imshow("Free Fire Gesture Control", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

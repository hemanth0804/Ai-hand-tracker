import cv2

def draw_text(frame, text, position=(50, 50), font_scale=1, color=(0, 255, 0), thickness=2):
    """Draws text on the frame."""
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 
                font_scale, color, thickness, cv2.LINE_AA)

def draw_circle(frame, center, radius=5, color=(0, 0, 255), thickness=-1):
    """Draws a circle at the given position (used for landmarks)."""
    cv2.circle(frame, center, radius, color, thickness)

def is_finger_up(landmarks, finger_tip_index, finger_base_index):
    """Checks if a finger is raised based on its tip and base y-coordinates."""
    if len(landmarks) > finger_tip_index and len(landmarks) > finger_base_index:
        return landmarks[finger_tip_index][1] < landmarks[finger_base_index][1]
    return False

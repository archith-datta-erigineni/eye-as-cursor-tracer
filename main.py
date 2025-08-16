import cv2
import mediapipe as mp
import pyautogui
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
pyautogui.moveTo(int(screen_w/2),int(screen_h/2))
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        a = int(landmarks[159].x * frame_w)
        b = int(landmarks[159].y * frame_h)
        c = int(landmarks[475].x * frame_w)
        d = int(landmarks[475].y * frame_h)
        cv2.circle(frame, (a, b), 3, (0, 0, 255))
        for id, landmark in enumerate(landmarks[474:478]):
            x = int((landmark.x) * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,0,255))
            if id == 1:
                screen_x = int((landmark.x-(landmark.x-landmarks[168].x))*screen_w)
                screen_y = int(landmark.y*screen_h)
                pyautogui.moveTo(int(screen_x),int(screen_y))




    cv2.imshow('Eye Tracer', frame)
    cv2.waitKey(1)
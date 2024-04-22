import cv2
import mediapipe as mp

# Initialize mediapipe hands module
mphands = mp.solutions.hands
mpdrawing = mp.solutions.drawing_utils

# Specify the path to your video file
vids =[
    '/home/stevend/Documents/Notebooks/Dia1/videos/mano1.mp4',
    '/home/stevend/Documents/Notebooks/Dia1/videos/mano2.mp4',
    '/home/stevend/Documents/Notebooks/Dia1/videos/mano3.mp4',
    '/home/stevend/Documents/Notebooks/Dia1/videos/mano4.mp4',
    '/home/stevend/Documents/Notebooks/Dia1/videos/mano5.mp4',
    '/home/stevend/Documents/Notebooks/Dia1/videos/parkinzon.mp4',
    '/home/stevend/Documents/Notebooks/Dia1/videos/dedo_gatillo.mp4'
]
vidpath = vids[6]

# Initialize video capture
vidcap = cv2.VideoCapture(vidpath)

# Set the desired window width and height
winwidth = 350
winheight = 600

# Initialize hand tracking
with mphands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame for hand tracking
        processFrames = hands.process(rgb_frame)

        # Draw landmarks on the frame
        if processFrames.multi_hand_landmarks:
            for lm in processFrames.multi_hand_landmarks:
                mpdrawing.draw_landmarks(frame, lm, mphands.HAND_CONNECTIONS)

        # Resize the frame to the desired window size
        resized_frame = cv2.resize(frame, (winwidth, winheight))

        # Display the resized frame
        cv2.imshow('Hand Tracking', resized_frame)

        # Exit loop by pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture and close windows
vidcap.release()
cv2.destroyAllWindows()
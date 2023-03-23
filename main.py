import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

prev_landmarks = None
prev_directions = None
prev_time = None

# initializing the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_frame_timestamp = cap.get(cv2.CAP_PROP_POS_MSEC)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    # drawing both the landmarks (points) and the connections (lines) between them
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    if results.pose_landmarks is not None:
        landmarks = np.array([(lmk.x, lmk.y, lmk.z) for lmk in results.pose_landmarks.landmark]).flatten()

        if prev_landmarks is not None:
            # dt is the time difference between the current and previous frames
            dt = (current_frame_timestamp - prev_time) / 1000  # milliseconds to seconds
            # speeds: difference between the current and previous positions divided by the frames time difference
            speeds = np.abs(landmarks - prev_landmarks) / dt
            # direction of movement of each landmark (relative to the previous frame)
            directions = np.array([landmarks[i:i+3] - prev_landmarks[i:i+3] for i in range(0, len(landmarks), 3)])
            directions_norm = np.apply_along_axis(lambda x: x / np.linalg.norm(x), 1, directions)
        else:
            speeds = np.zeros_like(landmarks)
            directions_norm = np.zeros((len(landmarks) // 3, 3))

        mean_speeds = np.mean(speeds.reshape((-1, 3)), axis=0)

        direction_votes = np.zeros(len(directions_norm))
        for i, direction in enumerate(directions_norm):
            dot_product = np.dot(direction, np.array([0, 0, 1]))  # compare with the z-axis
            if dot_product > 0:
                direction_votes[i] = 1  # "moving forward"
            else:
                direction_votes[i] = -1  # "moving backward"

        # majority vote of the directions to determine the overall direction of movement
        majority_vote = np.sign(np.sum(direction_votes))
        if majority_vote > 0:
            cv2.putText(image, "You are moving forwards", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        elif majority_vote < 0:
            cv2.putText(image, "You are moving backwards", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            cv2.putText(image, "You are not moving", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        prev_landmarks = landmarks
        prev_directions = directions_norm
        prev_time = current_frame_timestamp

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f"Mean Speed (x, y, z): {mean_speeds[0]:.2f}, {mean_speeds[1]:.2f}, {mean_speeds[2]:.2f} m/s",
                    (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("This is your webcam :)", image)

        # quit
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()



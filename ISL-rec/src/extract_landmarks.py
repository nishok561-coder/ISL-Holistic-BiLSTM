"""
=========================================================
Project : ISL Non-Manual Feature Recognition
File    : extract_landmarks.py
Purpose : Test MediaPipe Holistic on one video
=========================================================
"""

import cv2
import mediapipe as mp

import config as cfg
from logger import logger
from utils import load_master_metadata


# ==========================================================
# MediaPipe Initialization
# ==========================================================

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils


def main():

    logger.info("Loading metadata...")

    metadata = load_master_metadata(cfg.MASTER_METADATA)

    logger.info("Selecting first video...")

    first_video = metadata.iloc[0]["video_path"]

    logger.info(f"Video : {first_video}")

    cap = cv2.VideoCapture(first_video)

    if not cap.isOpened():
        logger.error("Unable to open video.")
        return

    with mp_holistic.Holistic(
        static_image_mode=False,
        model_complexity=1,
        smooth_landmarks=True,
        min_detection_confidence=cfg.MIN_DETECTION_CONFIDENCE,
        min_tracking_confidence=cfg.MIN_TRACKING_CONFIDENCE,
    ) as holistic:

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = holistic.process(rgb)

            # Face
            mp_drawing.draw_landmarks(
                frame,
                results.face_landmarks,
                mp_holistic.FACEMESH_CONTOURS,
            )

            # Pose
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_holistic.POSE_CONNECTIONS,
            )

            # Left Hand
            mp_drawing.draw_landmarks(
                frame,
                results.left_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
            )

            # Right Hand
            mp_drawing.draw_landmarks(
                frame,
                results.right_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS,
            )

            cv2.imshow("MediaPipe Holistic", frame)

            key = cv2.waitKey(10)

            if key == ord("q"):
                break

    cap.release()

    cv2.destroyAllWindows()

    logger.info("Finished.")


if __name__ == "__main__":
    main()
"""
=========================================================
Project : ISL Non-Manual Feature Recognition
File    : utils.py
Purpose : Common utility functions
=========================================================
"""

import cv2
import pandas as pd


def read_excel(file_path):
    """Read an Excel file."""
    return pd.read_excel(file_path)


def video_exists(video_path):
    """Check whether a video exists."""
    return video_path.exists()


def get_video_info(video_path):
    """
    Extract basic information from a video.

    Returns
    -------
    dict
    """

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        return None

    fps = cap.get(cv2.CAP_PROP_FPS)

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration = frames / fps if fps > 0 else 0

    cap.release()

    return {
        "fps": fps,
        "frames": frames,
        "duration": duration,
        "width": width,
        "height": height,
    }
    
def load_master_metadata(file_path):
    """
    Load the master metadata CSV.
    """
    return pd.read_csv(file_path)
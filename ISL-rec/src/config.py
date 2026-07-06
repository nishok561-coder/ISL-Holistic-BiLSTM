"""
=========================================================
Project : ISL Non-Manual Feature Recognition
File    : config.py
Purpose : Global configuration
=========================================================
"""

from pathlib import Path

# =========================================================
# PROJECT ROOT
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =========================================================
# DATA DIRECTORIES
# =========================================================

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

METADATA_DIR = DATA_DIR / "metadata"

LANDMARK_DIR = DATA_DIR / "landmarks"

PROCESSED_DIR = DATA_DIR / "processed"

MODEL_DIR = PROJECT_ROOT / "models"

RESULT_DIR = PROJECT_ROOT / "results"

# =========================================================
# DATASET PATHS
# =========================================================

DATASET_DIR = RAW_DATA_DIR / "ISL_CSLRT_Corpus"

VIDEO_DIR = DATASET_DIR / "Videos_Sentence_Level"

FRAME_DIR = DATASET_DIR / "Frames_Sentence_Level"

CSV_DIR = DATASET_DIR / "corpus_csv_files"

# =========================================================
# METADATA FILES
# =========================================================

DATASET_DETAILS = CSV_DIR / "ISL_CSLRT_Corpus details.xlsx"

FRAME_DETAILS = CSV_DIR / "ISL_CSLRT_Corpus_frame_details.xlsx"

WORD_DETAILS = CSV_DIR / "ISL_CSLRT_Corpus_word_details.xlsx"

GLOSS_FILE = CSV_DIR / "ISL Corpus sign glosses.csv"

MASTER_METADATA = METADATA_DIR / "master_metadata.csv"

# =========================================================
# MEDIAPIPE SETTINGS
# =========================================================

MIN_DETECTION_CONFIDENCE = 0.5

MIN_TRACKING_CONFIDENCE = 0.5

# =========================================================
# TRAINING SETTINGS
# =========================================================

MAX_SEQUENCE_LENGTH = 100

TRAIN_SPLIT = 0.80

RANDOM_SEED = 42

BATCH_SIZE = 16

EPOCHS = 50

LEARNING_RATE = 1e-3

# =========================================================
# CREATE REQUIRED DIRECTORIES
# =========================================================

DIRECTORIES = [
    METADATA_DIR,
    LANDMARK_DIR,
    PROCESSED_DIR,
    MODEL_DIR,
    RESULT_DIR,
]

for directory in DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)
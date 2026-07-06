"""
=========================================================
Project : ISL Non-Manual Feature Recognition
File    : dataset_explorer.py
Purpose : Build master metadata for the project
=========================================================
"""

import pandas as pd
from pathlib import Path

import config as cfg
from logger import logger
from utils import read_excel, get_video_info


def main():

    logger.info("Loading dataset metadata...")

    df = read_excel(cfg.DATASET_DETAILS)

    logger.info(f"Loaded {len(df)} records.")

    metadata = []

    for _, row in df.iterrows():

        sentence = row["Sentences"]

        relative_path = Path(row["File location"])

        # Convert relative path to absolute path
        video_path = cfg.RAW_DATA_DIR / relative_path

        exists = video_path.exists()

        fps = None
        frames = None
        duration = None
        width = None
        height = None

        if exists:

            info = get_video_info(video_path)

            if info is not None:

                fps = info["fps"]
                frames = info["frames"]
                duration = info["duration"]
                width = info["width"]
                height = info["height"]

        metadata.append(
            {
                "sentence": sentence,
                "video_name": video_path.name,
                "video_path": str(video_path),
                "exists": exists,
                "fps": fps,
                "frames": frames,
                "duration": duration,
                "width": width,
                "height": height,
            }
        )

    metadata_df = pd.DataFrame(metadata)

    metadata_df.to_csv(cfg.MASTER_METADATA, index=False)

    logger.info("===================================")
    logger.info(f"Total Videos : {len(metadata_df)}")
    logger.info(f"Classes      : {metadata_df['sentence'].nunique()}")
    logger.info(f"Missing      : {(~metadata_df['exists']).sum()}")
    logger.info("===================================")

    logger.info(f"Metadata saved to:\n{cfg.MASTER_METADATA}")


if __name__ == "__main__":
    main()
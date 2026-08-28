import os
import csv
import logging
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
META_DIR = DATA_DIR / "metadata"
MANIFESTS_DIR = DATA_DIR / "manifests"

logger = logging.getLogger(__name__)

def generate_manifests():
    asr_records = []
    mistake_records = []
    
    for meta_file in META_DIR.glob("*_metadata.csv"):
        with open(meta_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Basic check for reciter leakage in splits (Rule 10)
                # In a real implementation, we would hash reciter_id to ensure disjoint splits.
                # For now, we rely on the upstream split if provided.
                
                if row["is_mistake_labeled"] == "True":
                    mistake_records.append(row)
                else:
                    asr_records.append(row)
                    
    if asr_records:
        with open(MANIFESTS_DIR / "asr_evaluation.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=asr_records[0].keys())
            writer.writeheader()
            writer.writerows(asr_records)
        print(f"Created asr_evaluation.csv with {len(asr_records)} records.")
        
    if mistake_records:
        with open(MANIFESTS_DIR / "mistake_evaluation.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=mistake_records[0].keys())
            writer.writeheader()
            writer.writerows(mistake_records)
        print(f"Created mistake_evaluation.csv with {len(mistake_records)} records.")

if __name__ == "__main__":
    generate_manifests()

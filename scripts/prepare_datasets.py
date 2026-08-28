import os
import csv
import logging
import argparse
import re
from pathlib import Path

# Setup directories
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
META_DIR = DATA_DIR / "metadata"
MANIFESTS_DIR = DATA_DIR / "manifests"
LICENSES_DIR = DATA_DIR / "LICENSES"
INVENTORY_FILE = DATA_DIR / "DATASET_INVENTORY.md"

for d in [RAW_DIR, META_DIR, MANIFESTS_DIR, LICENSES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

SCHEMA = [
    "recording_id", "dataset_name", "file_path", "reciter_id", 
    "surah", "ayah", "word_id", "transcription", 
    "duration", "split", "source_license",
    "is_mistake_labeled", "original_label"
]

def setup_logger():
    logging.basicConfig(
        filename=DATA_DIR / "preparation.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

logger = setup_logger()

def parse_inventory(inventory_path):
    approved_datasets = []
    rejected_datasets = []
    
    with open(inventory_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Simple markdown table parser to find dataset blocks
    # Look for "#### <number>. <Dataset Name>"
    sections = re.split(r'#### \d+\.\s+', content)
    for section in sections[1:]:
        lines = section.strip().split('\n')
        name_line = lines[0]
        dataset_name = re.sub(r'[\:*?"<>|]', "", name_line).strip().split('(')[0].strip()
        
        status = None
        ds_type = None
        
        for line in lines:
            if "**verification_status**" in line:
                if "APPROVED" in line:
                    status = "APPROVED"
                elif "NEEDS_REVIEW" in line:
                    status = "NEEDS_REVIEW"
            if "**dataset_type**" in line:
                if "asr_correct" in line:
                    ds_type = "asr_correct"
                elif "mistake_labeled" in line:
                    ds_type = "mistake_labeled"
                    
        if status == "APPROVED":
            approved_datasets.append({"name": dataset_name, "type": ds_type})
        else:
            rejected_datasets.append({"name": dataset_name, "status": status})
            
    return approved_datasets, rejected_datasets

def download_and_parse_sample(dataset, sample_mode=False):
    """
    In a real implementation, this function would use the `datasets` library 
    (for Hugging Face) or `requests` to download the actual data.
    
    If sample_mode is True, we would stream only the first N rows from HF,
    or use a HEAD request for archives.
    
    Because this is a safe synthetic test (Rule 12), we will NOT download real data.
    We will create a synthetic metadata file that explicitly marks itself as synthetic.
    We will NOT claim to have processed real recordings unless they exist locally (Rule 2).
    """
    name = dataset["name"]
    ds_type = dataset["type"]
    logger.info(f"Preparing dataset: {name} (Type: {ds_type})")
    
    dataset_raw = RAW_DIR / name.replace(" ", "_")
    dataset_raw.mkdir(exist_ok=True)
    
    # Write Synthetic License (Rule 7: In reality, we'd fetch the real LICENSE file from the repo)
    with open(LICENSES_DIR / f"{name.replace(' ', '_')}.txt", "w", encoding="utf-8") as f:
        f.write("SYNTHETIC_TEST_LICENSE_FILE_NOT_REAL\n(In production, this is downloaded directly from the source repository)")
        
    # Write Synthetic Metadata (Rule 3: explicitly label it as synthetic)
    meta_path = META_DIR / f"{name.replace(' ', '_')}_metadata.csv"
    
    with open(meta_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writeheader()
        
        if sample_mode:
            # Generate exactly 1 synthetic record clearly marked as fake.
            file_name = "SYNTHETIC_TEST_RECORDING_DOES_NOT_EXIST.wav"
            
            writer.writerow({
                "recording_id": f"SYNTHETIC_{name.replace(' ', '_')}_001",
                "dataset_name": name,
                "file_path": f"raw/{name.replace(' ', '_')}/{file_name}",
                "reciter_id": "SYNTHETIC_RECITER",
                "surah": "1",
                "ayah": "1",
                "word_id": "",
                "transcription": "SYNTHETIC_TRANSCRIPTION",
                "duration": "0.0",
                "split": "test",
                "source_license": "SYNTHETIC",
                "is_mistake_labeled": "True" if ds_type == "mistake_labeled" else "False",
                "original_label": "SYNTHETIC_ORIGINAL_LABEL"
            })
            logger.info(f"[{name}] Generated synthetic test metadata. No real recordings downloaded.")
        else:
            logger.error(f"[{name}] Full download is blocked for safety. Use --sample.")

def main():
    parser = argparse.ArgumentParser(description="Prepare Quran Atlas datasets.")
    parser.add_argument("--sample", action="store_true", help="Run in safe sample/synthetic test mode.")
    args = parser.parse_args()
    
    logger.info("Starting Dataset Preparation")
    
    approved, rejected = parse_inventory(INVENTORY_FILE)
    
    logger.info(f"Found {len(approved)} APPROVED datasets.")
    for ds in approved:
        logger.info(f" - {ds['name']} ({ds['type']})")
        download_and_parse_sample(ds, sample_mode=args.sample)
        
    logger.info(f"Automatically rejected {len(rejected)} unapproved datasets.")
    for ds in rejected:
        logger.info(f" - REJECTED: {ds['name']} (Status: {ds['status']})")
        
    logger.info("Dataset Preparation Complete.")

if __name__ == "__main__":
    main()

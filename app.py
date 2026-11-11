#!/usr/bin/env python3
"""
ROCm Vision OCR — AMD AI League Match 2 Entrypoint (/app/app.py)
Accepts an image path or directory and outputs exact recognized text on AMD ROCm.
"""
import argparse
import json
import os
import time
from ocr_engine import ROCmOCREngine

def main():
    parser = argparse.ArgumentParser(description="ROCm Vision OCR — Match 2")
    parser.add_argument("--image", "-i", "--input", dest="image", default="", help="Path to input image or folder")
    parser.add_argument("--query-id", "--id", dest="query_id", default="ocr_001", help="Unique evaluation ID")
    parser.add_argument("--prompt", "-p", default="Extract the exact text on the license plate or sign.", help="OCR instruction")
    parser.add_argument("--output", "-o", default="", help="Explicit JSON output file path")
    parser.add_argument("--output-dir", default="/app/output", help="Output folder")
    args = parser.parse_args()

    out_dir = args.output_dir if os.access("/", os.W_OK) else "output"
    os.makedirs(out_dir, exist_ok=True)
    t0 = time.perf_counter()
    engine = ROCmOCREngine()
    res = engine.recognize(image_path=args.image, query_id=args.query_id, prompt=args.prompt)
    res["latency_sec"] = round(time.perf_counter() - t0, 4)

    out_path = args.output or os.path.join(out_dir, f"{args.query_id}_output.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
ROCm Vision OCR — Mini-Challenge 2 Official Entrypoint (/app/app.py)
Invocation: python3 /app/app.py --input-image /app/input/image_01.png
Writes: /app/output/image_01_output.json with {"text": "7ABC123", "confidence": 0.94}
"""
import argparse
import json
import os
from ocr_engine import ROCmOCREngine

DEFAULT_OUTPUT_DIR = os.environ.get("MC2_OUTPUT_DIR", "/app/output")

def main():
    p = argparse.ArgumentParser(description="ROCm Vision OCR — Mini-Challenge 2")
    p.add_argument("--input-image", "--image", "-i", "--input", dest="input_image", required=True, help="Path to input PNG, JPEG, or TIFF image")
    p.add_argument("--output", "-o", default="", help="Optional explicit output JSON path")
    p.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="Output directory")
    args, _ = p.parse_known_args()

    res = ROCmOCREngine().recognize(args.input_image)
    output_obj = {
        "text": str(res.get("text", "")),
        "confidence": float(res.get("confidence", 0.94)),
    }

    stem = os.path.splitext(os.path.basename(args.input_image))[0]
    out_dir = args.output_dir if os.access("/", os.W_OK) or args.output_dir != "/app/output" else "output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = args.output or os.path.join(out_dir, f"{stem}_output.json")
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output_obj, f, indent=2, ensure_ascii=False)
    print(json.dumps(output_obj, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
    main()

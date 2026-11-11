# ROCm Vision OCR — Sub-Second VLM Plate, Sign & Label Recognition on AMD Instinct MI300X

Built for **AMD AI League Match 2: Optical Character Recognition (`+1,200 XP`)** by **Tusiime Eriya** (`ERIX-12`).

## Architecture on AMD ROCm (`rocm/pytorch`)
- **Resident VLM Unix-Socket Server (`daemon_rocm.py`):** Loads `Qwen/Qwen2.5-VL-7B-Instruct` once in `bfloat16` on the AMD Instinct MI300X GPU (`192 GB HBM3`) behind `/tmp/rocm_ocr.sock`, avoiding 15s cold-start penalties on per-image CLI calls.
- **Adaptive Region-of-Interest (ROI) Contrast Normalizer (`ocr_engine.py`):** Crops, deskews, and sharpens license plates, road signs, and industrial equipment labels before VLM token decoding.
- **Strict Alphanumeric Post-Filter:** Strips conversational filler and outputs the exact recognized text string and bounding confidence to `/app/output/<image-id>_output.json.

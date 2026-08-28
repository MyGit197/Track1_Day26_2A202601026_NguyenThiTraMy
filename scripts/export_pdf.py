#!/usr/bin/env python3
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUBMISSION_DIR = ROOT / "submissions" / "2A202601026_NguyenThiTraMy"
HTML_PATH = SUBMISSION_DIR / "dashboard.html"

EDGE_PATH = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
if not EDGE_PATH.exists():
    EDGE_PATH = Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe")

pdf_targets = [
    SUBMISSION_DIR / "2A202601026_NguyenThiTraMy_Day26_dashboard.pdf",
    SUBMISSION_DIR / "NguyenThiTraMy_Day26_dashboard.pdf",
    ROOT / "2A202601026_NguyenThiTraMy_Day26_dashboard.pdf",
    ROOT / "NguyenThiTraMy_Day26_dashboard.pdf"
]

print(f"Generating PDFs from {HTML_PATH}...")
for target in pdf_targets:
    cmd = [
        str(EDGE_PATH),
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={target}",
        str(HTML_PATH)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if target.exists():
        print(f"SUCCESS: Generated {target} ({target.stat().st_size} bytes)")
    else:
        print(f"ERROR generating {target}: {res.stderr}")

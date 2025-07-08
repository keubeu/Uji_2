import json
import os
from datetime import datetime

# === Load resume_log.json ===
with open("resume_log.json", "r") as file:
    resume = json.load(file)

log_files = []
for kategori in resume["log_files"].values():
    log_files.extend(kategori)

log_last = resume["log_terakhir_diperbarui"]

# === Cek apakah file log tersedia ===
status = {}
for f in log_files:
    if not os.path.exists(f):
        status[f] = "MISSING"
    else:
        status[f] = "OK"

# === Cek apakah file terbaru sesuai resume ===
try:
    latest_file = max(
        [f for f in log_files if os.path.exists(f)],
        key=lambda f: os.path.getmtime(f)
    )
    latest_name = os.path.basename(latest_file)
    if latest_name != log_last:
        status[latest_name] = "OUTDATED"
except:
    pass

# === Simpan ke status.json ===
with open("status.json", "w") as out:
    json.dump(status, out, indent=2)

print("✅ Log checker selesai. Hasil disimpan ke status.json")

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

# === Simpan ke status.json ===
with open("status.json", "w") as out:
    json.dump(status, out, indent=2)

# === Hitung status sistem ===
total_log = len(log_files)
missing_count = sum(1 for status in status.values() if status == "MISSING")
outdated_count = sum(1 for status in status.values() if status == "OUTDATED")
is_synced = (missing_count == 0 and outdated_count == 0)

# === Buat system_status.json ===
system_status = {
    "sistem": "aktif",
    "jumlah_log": total_log,
    "log_terakhir_diperbarui": log_last,
    "log_tidak_ditemukan": missing_count,
    "sinkron": is_synced,
    "status": "stabil" if is_synced else "terganggu",
    "catatan": "Semua log valid dan sinkron." if is_synced else "Beberapa log hilang atau kedaluwarsa."
}

with open("system_status.json", "w") as sysfile:
    json.dump(system_status, sysfile, indent=2)

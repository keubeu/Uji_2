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
    existing_files = [f for f in log_files if os.path.exists(f)]
    if existing_files:
        latest_file = max(existing_files, key=lambda f: os.path.getmtime(f))
        latest_name = os.path.basename(latest_file)
        if latest_name != log_last:
            status[latest_name] = "OUTDATED"
except Exception as e:
    print(f"⚠️ Gagal memeriksa log terbaru: {e}")

# === Simpan ke status.json ===
with open("status.json", "w") as out:
    json.dump(status, out, indent=2)

print("✅ Log checker selesai. Hasil disimpan ke status.json")

# === Hitung status sistem ===
total_log = len(log_files)
missing_files = [f for f, s in status.items() if s == "MISSING"]
outdated_files = [f for f, s in status.items() if s == "OUTDATED"]
missing_count = len(missing_files)
outdated_count = len(outdated_files)
is_synced = (missing_count == 0 and outdated_count == 0)

# === Buat system_status.json ===
system_status = {
    "sistem": "aktif",
    "jumlah_log": total_log,
    "log_terakhir_diperbarui": log_last,
    "log_tidak_ditemukan": missing_count,
    "log_kedaluwarsa": outdated_count,
    "sinkron": is_synced,
    "status": "stabil" if is_synced else "terganggu",
    "catatan": "Semua log valid dan sinkron." if is_synced else "Beberapa log hilang atau kedaluwarsa.",
    "waktu_diperiksa": datetime.now().isoformat(),
    "daftar_log_hilang": missing_files,
    "daftar_log_kedaluwarsa": outdated_files
}

with open("system_status.json", "w") as sysfile:
    json.dump(system_status, sysfile, indent=2)

print("📄 system_status.json berhasil dibuat.")

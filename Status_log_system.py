import json
from uuid import uuid4
from datetime import datetime
import os

# ====== STATUS LEVEL ======
STATUS_LAPAR = ["kenyang", "normal", "lapar", "kelaparan"]
STATUS_HAUS = ["terhidrasi", "normal", "haus", "dehidrasi"]

# ====== UTILITAS STATUS ======
def turun_status(status, level):
    index = level.index(status)
    return level[min(index + 1, len(level) - 1)]

def naik_status(status, level):
    index = level.index(status)
    return level[max(index - 1, 0)]

# ====== MEMBUAT LOG STATUS ======
def buat_log_status(karakter_id, jenis, dari, menjadi, penyebab, arc, catatan=""):
    return {
        "log_id": f"status_{uuid4().hex[:6]}",
        "karakter_id": karakter_id,
        "jenis": jenis,
        "dari": dari,
        "menjadi": menjadi,
        "penyebab": penyebab,
        "arc": arc,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "catatan": catatan
    }

# ====== FUNGSI UPDATE STATUS ======
def update_status(karakter, jenis, level, penyebab, arc, catatan=""):
    sebelumnya = karakter[jenis]
    sesudah = turun_status(sebelumnya, level)
    karakter[jenis] = sesudah
    return buat_log_status(
        karakter_id=karakter.get("id", "UNKNOWN"),
        jenis=jenis,
        dari=sebelumnya,
        menjadi=sesudah,
        penyebab=penyebab,
        arc=arc,
        catatan=catatan
    )

# ====== SIMPAN LOG KE FILE JSON ======
def simpan_ke_log_sistem(log_baru, path="log_sistem.json"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {
            "sistem": "aktif",
            "jumlah_log": 0,
            "log_status": [],
            "log_tidak_ditemukan": 0,
            "sinkron": True,
            "status": "stabil",
            "catatan": "Log sistem baru dibuat."
        }

    # Tambah log baru
    data.setdefault("log_status", []).append(log_baru)
    data["jumlah_log"] = len(data["log_status"])
    data["log_terakhir_diperbarui"] = log_baru["timestamp"]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

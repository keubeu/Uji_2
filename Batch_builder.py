import json import os from datetime import datetime

=== Konfigurasi ===

RESUME_FILE = "Resume_log.json" CHARACTER_FILE = "character_log.json" EVENT_FILE = "event_log.json" DECISION_FILE = "decision_log.json" OUTPUT_FOLDER = "./"

=== Helper ===

def simpan_log(filename, data): with open(os.path.join(OUTPUT_FOLDER, filename), "w") as f: json.dump(data, f, indent=2) print(f"✅ {filename} berhasil dibuat.")

=== Load Resume ===

with open(RESUME_FILE, "r") as f: resume = json.load(f)

=== Load Known Characters dari character_log.json ===

known_characters = set() if os.path.exists(CHARACTER_FILE): with open(CHARACTER_FILE, "r") as f: characters = json.load(f) known_characters.update(c["id"] for c in characters)

=== Tambah karakter dari event_log dan decision_log ===

def extract_characters_from_log(file_path, field): ids = set() if os.path.exists(file_path): with open(file_path, "r") as f: data = json.load(f) for e in data.get("events", []): involved = e.get(field, []) ids.update(involved) return ids

known_characters.update(extract_characters_from_log(EVENT_FILE, "involved_characters")) known_characters.update(extract_characters_from_log(DECISION_FILE, "involved_characters"))

=== Validator karakter ===

def karakter_valid(cid): return cid in known_characters

=== Build: tracking_log.json ===

tracking = [] for cid, lokasi in resume.get("tracking_karakter", {}).items(): if not karakter_valid(cid): print(f"⚠️ Lewati {cid} — tidak dikenal secara sah.") continue entry = { "id": f"trk_{cid}", "subject_id": cid, "location": lokasi, "timestamp": resume["sesi_terakhir"]["waktu_terakhir_diperbarui"] } tracking.append(entry) simpan_log("tracking_log.json", tracking)

=== Build: inventory_log.json ===

inventaris = [] for idx, item in enumerate(resume.get("inventaris_utama", []), start=1): owner_id = "fig1" if not karakter_valid(owner_id): print(f"⚠️ Item {item} dilewati karena pemilik tidak sah: {owner_id}") continue entry = { "id": f"item{idx:02}", "owner_id": owner_id, "item_name": item, "quantity": 1 } inventaris.append(entry) simpan_log("inventory_log.json", inventaris)

=== Build: map_log.json ===

lokasi = resume.get("lokasi_terakhir", {}) map_log = { "date": resume["sesi_terakhir"]["waktu_terakhir_diperbarui"][:10], "regions": [ { "id": lokasi.get("kode", "unknown"), "name": lokasi.get("nama", "Lokasi Tidak Diketahui"), "type": lokasi.get("tipe", "tidak dikenal"), "description": lokasi.get("catatan", ""), "status": "dikuasai", "known_resources": [], "threat_level": resume["status_dunia"].get("ancaman_terdekat", "tidak diketahui") } ] } simpan_log("map_log.json", map_log)

=== Build: timeline_log.json ===

timeline_log = [ { "event_id": "evt_biosektor_escape", "datetime": resume["sesi_terakhir"]["waktu_terakhir_diperbarui"] } ] simpan_log("timeline_log.json", timeline_log)

print("\n📦 Batch builder selesai. Semua log utama dibentuk dari resume dengan proteksi karakter sah.")


# 🧾 Summary.md

## 🌐 Ringkasan Dunia dan Sistem Log Modular

Sistem ini adalah framework naratif realistis berbasis log modular. Setiap aspek dunia (karakter, konflik, diplomasi, waktu, status) dicatat secara terpisah, memungkinkan kesinambungan cerita dan interaksi AI secara otomatis.

---

## 📖 Narasi Dunia (Singkat)

Dunia sedang berada dalam masa pasca-kejatuhan, setelah keruntuhan sistem pemerintahan global. Faksi-faksi lokal mulai muncul untuk merebut wilayah dan sumber daya. Teknologi bertahan, tetapi kendali informasi dan kekuasaan tersebar. Konteks realistis tanpa makhluk fiksi, hanya manusia, hewan, dan sumber daya nyata.

Waktu naratif dibagi menjadi:
- `G` (Gelap → Malam)
- `N` (N terang → Siang/Pagi)

---

## 🧩 Komponen Modular

### 1. **Karakter**
- Tersimpan di: `character_log.json`
- Dilengkapi dengan `Status_karakter.json` (kesehatan, moral, lokasi)

### 2. **Faksi**
- Tersimpan di: `faction_log.json`
- Hubungan politik antar faksi: `diplomacy_log.json`

### 3. **Pertempuran & Misi**
- Catatan pertempuran: `battle_log.json`
- Keputusan penting: `decision_log.json`
- Pergerakan unit: `tracking_log.json`

### 4. **Ekonomi & Inventaris**
- Kekayaan & perdagangan: `economy_log.json`
- Barang dan senjata: `inventory_log.json`

### 5. **Pengetahuan & Riset**
- Peristiwa: `event_log.json`
- Penemuan & eksperimen: `research_log.json`

### 6. **Waktu dan Protokol**
- Transisi waktu: `timeline_log.json`
- Protokol global: `System_protokol.json`
- Sinkronisasi antar sistem: `protokol_log.json`
- Status sistem naratif: `Sistem_status_log.json`

### 7. **Narasi & Resume**
- Ringkasan cerita aktif: `Story_resume.log.json`
- Narasi interaktif (Twine): `story_log.twee`

---

## ✅ Validasi
Semua log diperiksa otomatis via `Log_checker.py` untuk memastikan:
- Format konsisten
- Field wajib ada (`id`, `timestamp`, `narrative_time`, `type`)
- Timestamp dalam format ISO8601

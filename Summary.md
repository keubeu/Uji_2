# 🧾 Summary.md

## 🌐 Ringkasan Dunia dan Sistem Log Modular

Proyek ini adalah sistem log naratif interaktif berbasis modular, yang memisahkan setiap aspek dunia ke dalam log spesifik untuk mendukung fleksibilitas, skalabilitas, dan keterbacaan oleh AI.

---

## 📖 Narasi Dunia (Singkat)

Sebuah dunia dinamis terbagi ke dalam faksi-faksi, karakter utama dan pendukung, peristiwa besar, dan konflik terbuka. Dunia ini berkembang berdasarkan keputusan yang diambil pemain dan AI narator, serta interaksi antar log (karakter, diplomasi, ekonomi, dsb).

---

## 🧩 Komponen Modular

### 1. **Karakter**
- Tersimpan di: `character_log.json`
- Mencakup: Nama, latar belakang, kondisi fisik dan mental, loyalitas, status emosi, dan hubungan.

### 2. **Faksi & Diplomasi**
- Tersimpan di: `faction_log.json`, `diplomacy_log.json`
- Menyimpan struktur, kekuatan, hubungan, perjanjian, dan konflik antar kelompok.

### 3. **Pertempuran & Keputusan**
- Tersimpan di: `battle_log.json`, `decision_log.json`
- Semua konflik tempur dan keputusan penting yang memengaruhi alur cerita.

### 4. **Ekonomi & Inventaris**
- Tersimpan di: `economy_log.json`, `inventory_log.json`
- Informasi tentang aset, sumber daya, item, serta transaksi ekonomi.

### 5. **Peta & Pelacakan**
- Tersimpan di: `map_log.json`, `tracking_log.json`
- Lokasi karakter, pergerakan, dan struktur dunia yang terekam secara spasial.

### 6. **Event & Timeline**
- Tersimpan di: `event_log.json`, `timeline_log.json`
- Semua peristiwa besar dan kronologi waktu secara linear.

### 7. **Ceritanya Sendiri**
- Tersimpan di: `story_log.twee`
- Format naratif cabang interaktif (Twine/Twee) sebagai kerangka cerita utama.

---

## ⚙️ Sistem & Validasi

### 🔧 File Sistem
- `System_protokol.json`: Protokol AI dan sistem pengatur perilaku log.
- `System_status.json`: Status terkini sinkronisasi dan keberadaan semua log.

### 📊 File Ringkasan
- `Resume_log.json`: Ringkasan menyeluruh untuk memuat ulang sesi AI.
- `resume_session.log`: Versi human-readable dari resume.
- `Summary.md`: Dokumen ini, sebagai pengingat sistem untuk pengembang/manajer dunia.

### 🧪 Pemeriksa & Antarmuka
- `Log_checker.py`: Memeriksa status log (hilang, outdated, rusak).
- `Index.html`: Tampilan log viewer untuk manusia.

---

## 🔄 Alur Sistem

```mermaid
flowchart TD
    start((Awal Sesi)) --> load[Load Resume_log.json]
    load --> check[Log_checker.py]
    check --> viewer[Index.html / Manual]
    viewer --> ai[AI Narasi Jalan]
    ai --> update[Update log masing-masing]
    update --> save[Simpan ke Resume_log.json lagi]
    save --> end((Sesi Berikutnya))

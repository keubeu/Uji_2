# 🧾 Summary.md

## 🌐 Ringkasan Dunia dan Sistem Log Modular

[Deskripsi umum tentang sistem dan tujuan penggunaannya.]

---

## 📖 Narasi Dunia (Singkat)

[Deskripsikan latar dunia: konflik utama, kondisi faksi, batas kekuasaan, status global, dan arah cerita.]

---

## 🧩 Komponen Modular

### 1. **Karakter**
- Tersimpan di: `character_log.json`
- Mencakup: [Isi — nama, latar belakang, kondisi fisik/mental, emosi, relasi, dll.]

### 2. **Faksi & Diplomasi**
- Tersimpan di: `faction_log.json`, `diplomacy_log.json`
- Mencakup: [Struktur faksi, afiliasi, hubungan antar kelompok, konflik diplomatik.]

### 3. **Pertempuran & Keputusan**
- Tersimpan di: `battle_log.json`, `decision_log.json`
- Mencakup: [Konflik bersenjata, duel, dan keputusan penting dalam narasi.]

### 4. **Ekonomi & Inventaris**
- Tersimpan di: `economy_log.json`, `inventory_log.json`
- Mencakup: [Sumber daya, barang, kekayaan, dan manajemen aset.]

### 5. **Peta & Pelacakan**
- Tersimpan di: `map_log.json`, `tracking_log.json`
- Mencakup: [Wilayah, lokasi karakter, pengaruh teritorial, dan pergerakan.]

### 6. **Event & Timeline**
- Tersimpan di: `event_log.json`, `timeline_log.json`
- Mencakup: [Peristiwa penting, urutan waktu, dan titik balik cerita.]

### 7. **Ceritanya Sendiri**
- Tersimpan di: `story_log.twee`
- Mencakup: [Struktur cerita cabang interaktif berbasis Twee (Twine).]

---

## ⚙️ Sistem & Validasi

### 🔧 File Sistem
- `System_protokol.json`: [Protokol AI internal dan aturan sistem naratif.]
- `System_status.json`: [Status sinkronisasi log aktif.]
- `Status_log_system.json`: [Status dan integritas sistem runtime.]

### 📊 File Ringkasan
- `Resume_log.json`: [Ringkasan semua log penting — digunakan oleh AI untuk melanjutkan sesi.]
- `resume_session.log`: [Ringkasan sesi aktif — versi untuk manusia.]
- `Summary.md`: [Dokumen manual ini — panduan teknis sistem log.]

### 🧪 Pemeriksa & Antarmuka
- `Log_checker.py`: [Script pemeriksa konsistensi log secara otomatis.]
- `Index.html`: [UI untuk menampilkan dan membaca semua log.]

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

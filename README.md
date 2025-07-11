# 📘 Sistem Log Modular AI — Dunia Naratif Interaktif

## 📂 Deskripsi Proyek

Sistem ini dirancang untuk mendukung dunia naratif interaktif berbasis AI melalui dokumentasi modular. Setiap elemen penting dalam dunia — mulai dari karakter, faksi, keputusan, hingga status sistem — direkam dalam log terpisah untuk memudahkan pelacakan, validasi otomatis, dan kelanjutan cerita secara dinamis.

---

## 📦 Struktur File Utama

| File                   | Fungsi                                   |
|------------------------|------------------------------------------|
| `battle_log.json`      | Catatan pertempuran dan konflik naratif  |
| `character_log.json`   | Status dan atribut karakter              |
| `decision_log.json`    | Rekaman keputusan penting                |
| `diplomacy_log.json`   | Hubungan antar faksi dan negosiasi       |
| `economy_log.json`     | Distribusi sumber daya dan kondisi ekonomi |
| `event_log.json`       | Peristiwa besar yang berdampak naratif   |
| `faction_log.json`     | Detail dan kondisi faksi-faksi           |
| `inventory_log.json`   | Daftar kepemilikan item dan aset         |
| `map_log.json`         | Peta wilayah, lokasi penting             |
| `protokol_log.json`    | Aturan atau hukum dalam dunia fiksi      |
| `research_log.json`    | Teknologi, penelitian, dan pengembangan  |
| `status_log.json`      | Status dunia saat ini                    |
| `story_log.twee`       | Alur cerita dalam format Twee            |
| `timeline_log.json`    | Kronologi kejadian naratif               |
| `tracking_log.json`    | Pelacakan tindakan dan interaksi AI-user |

---

## ⚙️ File Sistem & Kontrol

| File                      | Fungsi                                 |
|---------------------------|----------------------------------------|
| `System_protokol.json`    | Protokol internal sistem log           |
| `System_status.json`      | Status sistem dan sinkronisasi global  |
| `Status_log_system.json`  | Kondisi runtime sistem log saat ini    |
| `Resume_session_log.json` | Ringkasan log sesi aktif               |
| `Summary.md`              | Ringkasan manual naratif/log           |
| `Log_checker.py`          | Skrip untuk validasi struktur & isi log|
| `Index.html`              | Antarmuka visual log viewer            |
| `README.md`               | Dokumentasi proyek                     |

---

## 🧠 Fitur Utama

- **Modular:** Setiap file log berdiri sendiri dan mudah diproses
- **AI-Friendly:** Kompatibel dengan sistem AI naratif dan agent generatif
- **Auto Validation:** Struktur dan konten dapat diperiksa otomatis
- **Auto Resume:** Sistem mampu melanjutkan sesi naratif terakhir dari resume log

---

## 🚀 Cara Penggunaan

1. Tambahkan atau ubah file log JSON sesuai struktur standar.
2. Jalankan `Log_checker.py` untuk memvalidasi seluruh log.
3. Gunakan `Index.html` untuk menjelajah isi log secara visual.
4. Lanjutkan sesi naratif dengan memuat `Resume_session_log.json`.

---

## ⚠️ Catatan Pengembangan

- Pastikan setiap log menyertakan `metadata`, `timestamp`, dan `session_id`.
- Gunakan format waktu ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`).
- Semua file log harus divalidasi setelah perubahan manual.
- Protokol dunia (`protokol_log.json`) berbeda dengan status dunia (`status_log.json`): satu menetapkan aturan, yang lain mencerminkan kondisi aktual.

---

## ✍️ Dibuat oleh

_(Nama tim, studio, atau pengembang di sini)_

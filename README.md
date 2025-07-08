# 📘 Sistem Log Modular AI — Dunia Naratif Interaktif

## 📂 Deskripsi Proyek

Sistem ini adalah platform pencatatan modular menggunakan file JSON untuk mendukung dunia naratif interaktif. Semua log bersifat modular dan terstruktur agar dapat dibaca, dikelola, dan diperiksa oleh AI secara efisien.

---

## 📦 Struktur File Utama

| File                   | Fungsi |
|------------------------|--------|
| `battle_log.json`      | Catatan pertempuran dan konflik |
| `character_log.json`   | Status karakter (atribut, emosi, kondisi) |
| `decision_log.json`    | Catatan keputusan penting |
| `diplomacy_log.json`   | Hubungan antar faksi, diplomasi |
| `economy_log.json`     | Ekonomi, sumber daya, dan keuangan |
| `event_log.json`       | Daftar peristiwa penting |
| `faction_log.json`     | Informasi tentang faksi atau kelompok |
| `inventory_log.json`   | Inventaris dan item |
| `map_log.json`         | Lokasi, wilayah, peta dunia |
| `protokol_log.json`    | Protokol dunia non-sistem |
| `research_log.json`    | Teknologi/penelitian dalam dunia |
| `status_log.json`      | Kondisi umum dan status dunia |
| `story_log.twee`       | Alur cerita dalam format Twee |
| `timeline_log.json`    | Kronologi kejadian |
| `tracking_log.json`    | Pelacakan pergerakan atau interaksi karakter |

---

## ⚙️ File Sistem & Kontrol

| File                    | Fungsi |
|-------------------------|--------|
| `System_protokol.json`  | Protokol sistem dan AI |
| `System_status.json`    | Status sinkronisasi log |
| `Resume_log.json`       | Ringkasan global log untuk AI |
| `resume_session.log`    | Ringkasan sesi saat ini |
| `Summary.md`            | Ringkasan manual dunia dan sistem |
| `Log_checker.py`        | Pemeriksa konsistensi log |
| `Index.html`            | Tampilan antarmuka log viewer |
| `README.md`             | Dokumentasi proyek ini |

---

## 🧠 Fitur Utama

- **Modular**: Setiap log berdiri sendiri, bisa diubah atau diganti kapan saja.
- **AI-Friendly**: Format dan struktur kompatibel dengan sistem naratif AI.
- **Auto Validation**: Log checker otomatis mendeteksi log hilang atau usang.
- **Auto Resume**: AI dapat melanjutkan sesi narasi menggunakan `Resume_log.json`.

---

## 🚀 Cara Penggunaan

1. Tambahkan atau ubah log sesuai format standar `.json`.
2. Jalankan `Log_checker.py` untuk validasi otomatis.
3. Gunakan `Index.html` untuk melihat log melalui UI.
4. `Resume_log.json` dan `resume_session.log` digunakan oleh AI untuk melanjutkan sesi secara otomatis.

---

## ⚠️ Catatan Pengembangan

- Selalu sertakan field `metadata` di setiap log.
- Gunakan timestamp ISO 8601 (`YYYY-MM-DDTHH:MM:SSZ`) untuk waktu.
- Setelah perubahan manual, jalankan kembali `Log_checker.py`.

---

## ✍️ Dibuat oleh

Lucu (?) — 2025

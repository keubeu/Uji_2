# 🌐 Unity Log System

Sistem pencatatan dunia berbasis log modular.  
Dirancang untuk mendukung cerita interaktif, simulasi strategi, dan manajemen dunia secara berlapis.

Semua log disimpan di dalam direktori: `/logs/`

---

## 📚 Struktur File & Fungsi

| No. | Nama File              | Fungsi                                                                 |
|-----|------------------------|------------------------------------------------------------------------|
| 01  | `story_log.twee`       | Narasi utama cerita dalam format Twine (Twee)                          |
| 02  | `timeline_log.json`    | Catatan waktu harian: tanggal, pagi/malam, event                       |
| 03  | `character_log.json`   | Data karakter: nama, peran, status, asal, interaksi                    |
| 04  | `decision_log.json`    | Keputusan penting, opsi, dan konsekuensinya                             |
| 05  | `event_log.json`       | Peristiwa besar, insiden, atau konflik                                 |
| 06  | `map_log.json`         | Wilayah dunia, kontrol area, dan posisi strategis                      |
| 07  | `inventory_log.json`   | Daftar item, alat, senjata, bahan, lokasi, dan kondisi                 |
| 08  | `battle_log.json`      | Musuh, level ancaman, catatan pertempuran, status terkini              |
| 09  | `faction_log.json`     | Data kelompok/faksi: nama, aliansi, kekuatan, pengaruh                  |
| 10  | `diplomacy_log.json`   | Relasi antar faksi: status damai, netral, musuh                        |
| 11  | `economy_log.json`     | Pemasukan, pengeluaran, transaksi, dan harga pasar                     |
| 12  | `espionage_log.json`   | Operasi intelijen: target, hasil, tingkat deteksi                      |
| 13  | `research_log.json`    | Proyek riset, progres (%), unlock teknologi                            |
| 14  | `tracking_log.json`    | Pergerakan karakter, penampakan, jejak, pelacakan                      |
| 15  | `status_log.json`      | Laporan populasi, makanan, produksi, grafik perubahan harian           |
| 16  | `protokol_log.json`    | Daftar aturan sistem: musuh alami, diplomasi, penyimpanan otomatis     |
| 17  | `log_checker.json`     | Validasi status semua log (missing, empty, valid, damaged)             |
| 18  | `log_viewer.html`      | Penampil log interaktif berbasis browser                              |
| 19  | `Summary.md`           | Ringkasan per arc: peristiwa penting, konflik, keputusan                |
| 20  | `README.md`            | Dokumentasi sistem log ini                                             |

---

## 🧩 Prinsip Sistem

- **Modular**: Tiap aspek cerita/log dipisah dalam file berbeda
- **Efisien**: Format JSON minimalis, ringan untuk AI & sistem pembaca
- **Terbaca AI**: Semua log mengikuti struktur baku agar mudah diproses
- **Interaktif**: Dukungan Twine (`.twee`) & visualisasi HTML (`log_viewer.html`)

---

## 📦 Status Proyek

🟢 **Struktur log lengkap.**  
📄 Siap digunakan untuk simulasi cerita Unity atau sistem dunia sejenis.  
✍️ Data dasar masih dalam pengisian awal.

---

## 📎 Lisensi

Proyek ini bersifat **pribadi** untuk pengelolaan cerita interaktif.  
Tidak digunakan untuk distribusi publik tanpa izin eksplisit dari pengembang utama.

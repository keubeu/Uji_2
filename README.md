# 🧾 README.md

## 📌 Tujuan Sistem Log Modular Naratif
Sistem ini dirancang untuk mendukung dunia naratif interaktif berbasis realisme, dengan pencatatan otomatis dan modular dari setiap elemen penting dunia: karakter, pertempuran, diplomasi, keputusan, waktu, dan lain-lain. Semua file log diatur dalam format JSON untuk kompatibilitas AI, validasi otomatis, dan kesinambungan cerita jangka panjang.

---

## 📁 Struktur Berkas

### 📂 Log Utama (JSON)
Berikut daftar lengkap log yang digunakan:

| No | Nama Log                  | Fungsi |
|----|----------------------------|--------|
| 1  | `Story_resume.log.json`   | Ringkasan narasi hidup dan kontinuitas waktu naratif |
| 2  | `System_protokol.json`    | Protokol sistem naratif dan aturan dunia |
| 3  | `battle_log.json`         | Catatan pertempuran secara modular |
| 4  | `character_log.json`      | Data semua karakter beserta hubungan dan statusnya |
| 5  | `decision_log.json`       | Catatan semua keputusan penting yang memengaruhi cerita |
| 6  | `diplomacy_log.json`      | Hubungan diplomatik antar faksi atau kelompok |
| 7  | `economy_log.json`        | Sistem ekonomi, distribusi sumber daya, harga barang |
| 8  | `event_log.json`          | Peristiwa penting dunia (baik acak maupun skrip) |
| 9  | `faction_log.json`        | Daftar faksi dan status politiknya |
| 10 | `inventory_log.json`      | Catatan barang, senjata, logistik, dan pemilik |
| 11 | `map_log.json`            | Lokasi, wilayah, koordinat strategis |
| 12 | `protokol_log.json`       | Sinkronisasi lintas waktu dan sistem antar log |
| 13 | `research_log.json`       | Penelitian, kemajuan teknologi, dan eksperimen |
| 14 | `timeline_log.json`       | Urutan waktu dan transisi antara pagi (G) dan malam (N) |
| 15 | `tracking_log.json`       | Pergerakan unit, karakter, dan misi |
| 16 | `Sistem_status_log.json`  | Status sistem runtime (sinkronisasi, error, validasi) |
| 17 | `Status_karakter.json`    | Status kesehatan, moral, posisi terkini tiap karakter |

### 📂 Tools Pendukung
| Nama Berkas         | Fungsi |
|---------------------|--------|
| `README.md`         | Penjelasan sistem ini |
| `Summary.md`        | Ringkasan dunia dan struktur global |
| `Log_checker.py`    | Skrip Python untuk validasi log (format, field, relasi) |
| `Index.html`        | Dashboard UI modular untuk menampilkan log secara visual |
| `story_log.twee`    | File interaktif dari narasi (Twine compatible) |

---

## ⚙️ Validasi & Otomatisasi
- Semua log memiliki `required_fields` sesuai `System_protokol.json`
- Setiap log memiliki `timestamp`, `narrative_time` (G/N), dan validasi lintas log
- Disarankan menggunakan `Log_checker.py` sebelum setiap commit

---

## 🌐 Lisensi & Kontribusi
Struktur ini bersifat open development. Silakan sesuaikan dengan dunia buatanmu. Jika ingin berkontribusi, tambahkan dokumentasi dan buat validasi lintas log yang konsisten.

> Dibuat oleh sistem naratif modular AI | Versi: 1.0

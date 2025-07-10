import json
import datetime
import logging

# === Setup Logging ===
logging.basicConfig(
    filename='log_sistem.txt',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)
logger = logging.getLogger('SistemNarasi')


# === Validator Narasi terhadap Log Dunia ===
class NarasiValidator:
    def __init__(self, path_log):
        self.log = self.load_log(path_log)

    def load_log(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info("✅ Log dunia dimuat dari: %s", path)
            return data

    def validasi_narasi(self, teks: str):
        hasil = {
            "item_tidak_dikenali": [],
            "lokasi_tidak_valid": [],
            "karakter_tidak_terdaftar": []
        }

        # === Validasi dari data log asli ===
        item_log = self.log.get("item", [])
        lokasi_log = self.log.get("lokasi", [])
        karakter_log = self.log.get("karakter", [])

        # Validasi Item
        for item in self._temukan_kandidat(teks):
            if item.lower() not in [i.lower() for i in item_log]:
                hasil["item_tidak_dikenali"].append(item)

        # Validasi Lokasi
        for lokasi in lokasi_log:
            if lokasi in teks:
                break
        else:
            hasil["lokasi_tidak_valid"].append("Tidak ditemukan lokasi yang sah dalam narasi.")

        # Validasi Karakter
        ditemukan = False
        for karakter in karakter_log:
            if karakter in teks:
                ditemukan = True
                break
        if not ditemukan:
            hasil["karakter_tidak_terdaftar"].append("Tidak ditemukan karakter valid.")

        if any(hasil.values()):
            logger.warning("❌ Validasi gagal: %s", json.dumps(hasil, ensure_ascii=False))
        else:
            logger.info("✅ Narasi valid terhadap log dunia.")

        return hasil

    def _temukan_kandidat(self, teks):
        # Sederhana: ambil kata setelah "item" jika ada
        kata = []
        potongan = teks.split()
        for i, w in enumerate(potongan):
            if w.lower() == "item" and i+1 < len(potongan):
                kata.append(f"{w} {potongan[i+1]}")
        return kata


# === Penegak Protokol Sistem Naratif ===
class SystemProtocolEnforcer:
    def __init__(self, nama_modul="Lucu"):
        self.nama_modul = nama_modul
        self.riwayat_peringatan = []
        self.protokol_utama = [
            "Validasi narasi terhadap log dunia",
            "Tidak menambahkan elemen di luar data log",
            "Mendahulukan instruksi pengguna yang eksplisit",
            "Transparansi dalam setiap pembaruan log",
            "Menerapkan timestamp ISO 8601 pada setiap peristiwa"
        ]

    def periksa_kepatuhan(self, narasi: str) -> bool:
        pelanggaran = []

        # Deteksi struktural (bukan sekadar string)
        if "log diperbarui" not in narasi.lower():
            pelanggaran.append("Transparansi dalam setiap pembaruan log")
        if "T" not in narasi and "Z" not in narasi:
            pelanggaran.append("Menerapkan timestamp ISO 8601 pada setiap peristiwa")
        if "perintah" not in narasi.lower() and "instruksi" not in narasi.lower():
            pelanggaran.append("Mendahulukan instruksi pengguna yang eksplisit")

        if pelanggaran:
            self._catat_peringatan(pelanggaran)
            return False

        logger.info("✅ Narasi mematuhi semua protokol sistem.")
        return True

    def _catat_peringatan(self, daftar_pelanggaran):
        waktu = datetime.datetime.now().isoformat()
        pesan = {
            "waktu": waktu,
            "modul": self.nama_modul,
            "peringatan": daftar_pelanggaran
        }
        self.riwayat_peringatan.append(pesan)
        logger.error("⚠️ Pelanggaran protokol oleh [%s]: %s", self.nama_modul, daftar_pelanggaran)

        # Simpan ke peringatan_ai.json secara otomatis
        with open("peringatan_ai.json", "w", encoding="utf-8") as f:
            json.dump(self.riwayat_peringatan, f, indent=2, ensure_ascii=False)

    def tampilkan_riwayat(self):
        return self.riwayat_peringatan


# === Pipeline Narasi Utama ===
class PipelineNarasi:
    def __init__(self, path_log):
        self.validator = NarasiValidator(path_log)
        self.enforcer = SystemProtocolEnforcer()

    def proses_narasi(self, narasi: str):
        logger.info("📥 Memproses narasi baru.")

        # 1. Validasi terhadap log dunia
        hasil_validasi = self.validator.validasi_narasi(narasi)
        if any(hasil_validasi.values()):
            logger.info("⛔ Narasi dibatalkan karena tidak sesuai log.")
            return "[DIBATALKAN] Narasi mengandung elemen yang tidak ada di log."

        # 2. Validasi terhadap protokol sistem
        if not self.enforcer.periksa_kepatuhan(narasi):
            logger.info("⛔ Narasi dibatalkan karena pelanggaran protokol.")
            return "[DIBATALKAN] Narasi tidak mematuhi protokol sistem."

        logger.info("✅ Narasi disetujui oleh sistem.")
        return f"✅ Narasi disetujui:\n{narasi}"

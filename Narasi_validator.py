import json
import re
from datetime import datetime

class NarasiValidator:
    def __init__(self, path_log):
        self.log = self.load_log(path_log)

    def load_log(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def validasi_narasi(self, teks):
        hasil = {
            "item_tidak_dikenal": [],
            "karakter_tidak_dikenal": [],
            "lokasi_tidak_dikenal": [],
            "kemampuan_tidak_dikenal": []
        }
        teks_lower = teks.lower()
        for kategori in ["item", "karakter", "lokasi", "kemampuan"]:
            entri_log_lower = [e.lower() for e in self.log.get(kategori, [])]
            for kata in self.extract_frasa_kandidat(teks_lower):
                if kata in entri_log_lower:
                    continue
                if any(kata in e for e in entri_log_lower):
                    continue
                if kata.strip() != "":
                    hasil[f"{kategori}_tidak_dikenal"].append(kata)
        return hasil

    def extract_frasa_kandidat(self, teks):
        teks = re.sub(r"[^\w\s]", "", teks.lower())  # hilangkan tanda baca
        kata = teks.split()
        frasa = set()
        for i in range(len(kata)):
            frasa.add(kata[i])
            if i+1 < len(kata):
                frasa.add(f"{kata[i]} {kata[i+1]}")
            if i+2 < len(kata):
                frasa.add(f"{kata[i]} {kata[i+1]} {kata[i+2]}")
        return frasa

    def tampilkan_peringatan(self, hasil):
        timestamp = datetime.utcnow().isoformat()
        print(f"\n[SISTEM VALIDATOR]\nWaktu: {timestamp}Z")
        ada_pelanggaran = False
        for k, v in hasil.items():
            if v:
                ada_pelanggaran = True
                print(f"⚠️ {k.replace('_', ' ').capitalize()}: {sorted(set(v))}")
        if not ada_pelanggaran:
            print("✅ Narasi valid, tidak ditemukan pelanggaran.")

# ====== Contoh Penggunaan =======
if __name__ == "__main__":
    validator = NarasiValidator("resume_log.json")
    narasi = """
    Lucu dan Arin mengaktifkan drone pengintai saat mendekati Lembah Asing.
    Mereka menggunakan senapan plasma untuk mengamankan area.
    """
    hasil_validasi = validator.validasi_narasi(narasi)
    validator.tampilkan_peringatan(hasil_validasi)

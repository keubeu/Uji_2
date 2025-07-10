class NarasiValidator:
    def __init__(self, path_log):
        self.path_log = path_log  # Simpan path log untuk reload dinamis
        self.log = self.load_log(self.path_log)

    def load_log(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info("✅ Log dunia dimuat dari: %s", path)
            return data

    def validasi_narasi(self, teks: str):
        # Baca ulang log setiap kali validasi dilakukan
        self.log = self.load_log(self.path_log)

        hasil = {
            "item_tidak_dikenali": [],
            "lokasi_tidak_valid": [],
            "karakter_tidak_terdaftar": []
        }

        item_log = self.log.get("item", [])
        lokasi_log = self.log.get("lokasi", [])
        karakter_log = self.log.get("karakter", [])

        # Validasi Item
        for item in self._temukan_kandidat(teks):
            if item.lower() not in [i.lower() for i in item_log]:
                hasil["item_tidak_dikenali"].append(item)

        # Validasi Lokasi
        if not any(lokasi in teks for lokasi in lokasi_log):
            hasil["lokasi_tidak_valid"].append("Tidak ditemukan lokasi yang sah dalam narasi.")

        # Validasi Karakter
        if not any(karakter in teks for karakter in karakter_log):
            hasil["karakter_tidak_terdaftar"].append("Tidak ditemukan karakter valid.")

        if any(hasil.values()):
            logger.warning("❌ Validasi gagal: %s", json.dumps(hasil, ensure_ascii=False))
        else:
            logger.info("✅ Narasi valid terhadap log dunia.")

        return hasil

    def _temukan_kandidat(self, teks):
        # Deteksi sederhana item: ambil kata setelah "item"
        kata = []
        potongan = teks.split()
        for i, w in enumerate(potongan):
            if w.lower() == "item" and i+1 < len(potongan):
                kata.append(f"{w} {potongan[i+1]}")
        return kata

from produk_roti import ProdukRoti

class RotiTawar(ProdukRoti):
    def __init__(self, kode, nama, harga, stok, jenis_tepung, berat_gram, untuk_sandwich):
        super().__init__(kode, nama, harga, stok)
        self.__jenis_tepung = jenis_tepung
        self.__berat_gram = berat_gram
        self.__untuk_sandwich = untuk_sandwich

    def get_jenis_tepung(self):
        return self.__jenis_tepung

    def get_berat_gram(self):
        return self.__berat_gram

    def is_untuk_sandwich(self):
        return self.__untuk_sandwich

    def set_berat_gram(self, berat):
        if berat > 0:
            self.__berat_gram = berat

    
    def hitung_jumlah_lembar(self):
        """Perkiraan jumlah lembar (1 lembar ~ 30 gram)."""
        return self.__berat_gram // 30

    def saran_penyajian(self):
        if self.__untuk_sandwich:
            return "Cocok untuk sandwich dan roti panggang."
        return "Cocok disantap dengan selai atau mentega."

    
    def get_jenis(self):
        return "Roti Tawar"

    def tampilkan_info(self):
        return (super().tampilkan_info() +
                f" | Tepung: {self.__jenis_tepung} | {self.__berat_gram}g "
                f"(~{self.hitung_jumlah_lembar()} lembar)")

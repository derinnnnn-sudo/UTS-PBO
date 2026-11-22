from produk_roti import ProdukRoti

class RotiManis(ProdukRoti):
    def __init__(self, kode, nama, harga, stok, rasa_isi, level_manis, topping):
        super().__init__(kode, nama, harga, stok)
        self.__rasa_isi = rasa_isi
        self.__level_manis = level_manis  
        self.__topping = topping

    def get_rasa_isi(self):
        return self.__rasa_isi

    def get_level_manis(self):
        return self.__level_manis

    def get_topping(self):
        return self.__topping

    def set_level_manis(self, level):
        if 1 <= level <= 5:
            self.__level_manis = level

    
    def deskripsi_rasa(self):
        return f"Isi {self.__rasa_isi} dengan topping {self.__topping}."

    def kategori_manis(self):
        if self.__level_manis <= 2:
            return "Manis ringan"
        if self.__level_manis <= 4:
            return "Manis sedang"
        return "Sangat manis"

    
    def get_jenis(self):
        return "Roti Manis"

    def tampilkan_info(self):
        return (super().tampilkan_info() +
                f" | Isi: {self.__rasa_isi} | Topping: {self.__topping} | "
                f"{self.kategori_manis()} ({self.__level_manis}/5)")

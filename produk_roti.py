BATAS_STOK_MENIPIS = 5
class ProdukRoti:
    def __init__(self, kode, nama, harga, stok):
        self.__kode = kode
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    
    def get_kode(self):
        return self.__kode

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    
    def set_nama(self, nama):
        if nama.strip():
            self.__nama = nama.strip()

    def set_harga(self, harga):
        if harga >= 0:
            self.__harga = harga

    def set_stok(self, stok):
        if stok >= 0:
            self.__stok = stok


    def kurangi_stok(self, jumlah):
        """Kurangi stok saat terjual. Return True jika berhasil."""
        if 0 < jumlah <= self.__stok:
            self.__stok -= jumlah
            return True
        return False

    def hitung_harga_total(self, jumlah):
        return self.__harga * jumlah

    def cek_status(self):
        if self.__stok == 0:
            return "Habis"
        if self.__stok <= BATAS_STOK_MENIPIS:
            return "Stok menipis"
        return "Tersedia"

    def get_jenis(self):
        return "Roti"

    def tampilkan_info(self):
        return (f"[{self.__kode}] {self.__nama} ({self.get_jenis()}) | "
                f"Rp{self.__harga:,} | Stok: {self.__stok} | {self.cek_status()}")

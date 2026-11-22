class Penjualan:
    def __init__(self, id_penjualan, nama_pelanggan, tanggal):
        self.__id_penjualan = id_penjualan
        self.__nama_pelanggan = nama_pelanggan
        self.__tanggal = tanggal
        self.__daftar_item = []  

    def get_id(self):
        return self.__id_penjualan

    def get_nama_pelanggan(self):
        return self.__nama_pelanggan

    def get_tanggal(self):
        return self.__tanggal

    def get_daftar_item(self):
        return list(self.__daftar_item)

    def set_nama_pelanggan(self, nama):
        if nama.strip():
            self.__nama_pelanggan = nama.strip()


    def tambah_item(self, produk, jumlah):
        if produk.kurangi_stok(jumlah):
            self.__daftar_item.append((produk, jumlah))
            return True
        return False

    def hitung_total(self):
        return sum(p.hitung_harga_total(j) for p, j in self.__daftar_item)

    def jumlah_item(self):
        return sum(j for _, j in self.__daftar_item)

    def status_transaksi(self):
        return "Selesai" if self.__daftar_item else "Kosong"

    def tampilkan_info(self):
        baris = [f"[{self.__id_penjualan}] {self.__tanggal} | Pelanggan: "
                 f"{self.__nama_pelanggan} | Status: {self.status_transaksi()}"]
        for produk, jumlah in self.__daftar_item:
            baris.append(f"    - {produk.get_nama()} x{jumlah} = "
                         f"Rp{produk.hitung_harga_total(jumlah):,}")
        baris.append(f"    Total: Rp{self.hitung_total():,}")
        return "\n".join(baris)

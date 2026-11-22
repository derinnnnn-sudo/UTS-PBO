from datetime import date

from produk_roti import ProdukRoti
from roti_tawar import RotiTawar
from roti_manis import RotiManis
from penjualan import Penjualan

daftar_roti = [
    RotiTawar("RT01", "Roti Tawar Putih", 15000, 20, "Terigu protein tinggi", 400, True),
    RotiTawar("RT02", "Roti Tawar Gandum", 18000, 4, "Gandum utuh", 450, False),
    RotiManis("RM01", "Roti Cokelat", 7000, 15, "Cokelat", 3, "Meses"),
    RotiManis("RM02", "Roti Keju", 8000, 0, "Keju", 2, "Parutan keju"),
]
daftar_penjualan = []


def input_int(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("  ! Masukkan angka yang valid.")


def cari_roti(kode):
    for roti in daftar_roti:
        if roti.get_kode().lower() == kode.lower():
            return roti
    return None


def cari_penjualan(id_penjualan):
    for p in daftar_penjualan:
        if p.get_id().lower() == id_penjualan.lower():
            return p
    return None


def pilih_entitas():
    print("  1. Roti\n  2. Penjualan")
    return input("  Pilih data (1/2): ").strip()


def tambah_data():
    pilihan = pilih_entitas()
    if pilihan == "1":
        print("  Jenis roti: 1. Roti Tawar  2. Roti Manis")
        jenis = input("  Pilih jenis (1/2): ").strip()
        kode = input("  Kode roti : ").strip()
        if cari_roti(kode):
            print("  ! Kode sudah dipakai.")
            return
        nama = input("  Nama      : ").strip()
        harga = input_int("  Harga     : ")
        stok = input_int("  Stok      : ")
        if jenis == "1":
            tepung = input("  Jenis tepung       : ").strip()
            berat = input_int("  Berat (gram)       : ")
            sandwich = input("  Untuk sandwich (y/n): ").strip().lower() == "y"
            daftar_roti.append(RotiTawar(kode, nama, harga, stok, tepung, berat, sandwich))
        elif jenis == "2":
            rasa = input("  Rasa isi           : ").strip()
            level = input_int("  Level manis (1-5)  : ")
            topping = input("  Topping            : ").strip()
            daftar_roti.append(RotiManis(kode, nama, harga, stok, rasa, level, topping))
        else:
            print("  ! Jenis tidak valid.")
            return
        print("  Roti berhasil ditambahkan.")
    elif pilihan == "2":
        id_p = input("  ID penjualan   : ").strip()
        if cari_penjualan(id_p):
            print("  ! ID sudah dipakai.")
            return
        pelanggan = input("  Nama pelanggan : ").strip()
        transaksi = Penjualan(id_p, pelanggan, date.today().isoformat())
        print("  Tambahkan item (kosongkan kode untuk selesai):")
        while True:
            kode = input("   Kode roti : ").strip()
            if not kode:
                break
            roti = cari_roti(kode)
            if roti is None:
                print("   ! Roti tidak ditemukan.")
                continue
            jumlah = input_int("   Jumlah    : ")
            if transaksi.tambah_item(roti, jumlah):
                print(f"   + {roti.get_nama()} x{jumlah} ditambahkan.")
            else:
                print(f"   ! Stok tidak cukup (stok: {roti.get_stok()}).")
        if transaksi.jumlah_item() == 0:
            print("  ! Transaksi kosong, tidak disimpan.")
            return
        daftar_penjualan.append(transaksi)
        print(f"  Transaksi disimpan. Total: Rp{transaksi.hitung_total():,}")
    else:
        print("  ! Pilihan tidak valid.")


def tampilkan_data():
    pilihan = pilih_entitas()
    if pilihan == "1":
        if not daftar_roti:
            print("  (Belum ada data roti)")
        for roti in daftar_roti:
            print("  " + roti.tampilkan_info())
    elif pilihan == "2":
        if not daftar_penjualan:
            print("  (Belum ada transaksi)")
        for p in daftar_penjualan:
            print("  " + p.tampilkan_info().replace("\n", "\n  "))
    else:
        print("  ! Pilihan tidak valid.")


def cari_data():
    pilihan = pilih_entitas()
    kata = input("  Kata kunci (kode/nama): ").strip().lower()
    if pilihan == "1":
        hasil = [r for r in daftar_roti
                 if kata in r.get_kode().lower() or kata in r.get_nama().lower()]
        for r in hasil:
            print("  " + r.tampilkan_info())
    elif pilihan == "2":
        hasil = [p for p in daftar_penjualan
                 if kata in p.get_id().lower() or kata in p.get_nama_pelanggan().lower()]
        for p in hasil:
            print("  " + p.tampilkan_info().replace("\n", "\n  "))
    else:
        print("  ! Pilihan tidak valid.")
        return
    if not hasil:
        print("  Data tidak ditemukan.")


def ubah_data():
    pilihan = pilih_entitas()
    if pilihan == "1":
        roti = cari_roti(input("  Kode roti yang diubah: ").strip())
        if roti is None:
            print("  ! Roti tidak ditemukan.")
            return
        print("  " + roti.tampilkan_info())
        nama = input("  Nama baru (kosong = tetap)  : ").strip()
        harga = input("  Harga baru (kosong = tetap) : ").strip()
        stok = input("  Stok baru (kosong = tetap)  : ").strip()
        if nama:
            roti.set_nama(nama)
        if harga.isdigit():
            roti.set_harga(int(harga))
        if stok.isdigit():
            roti.set_stok(int(stok))
        print("  Data roti diperbarui.")
    elif pilihan == "2":
        p = cari_penjualan(input("  ID penjualan yang diubah: ").strip())
        if p is None:
            print("  ! Transaksi tidak ditemukan.")
            return
        nama = input("  Nama pelanggan baru: ").strip()
        p.set_nama_pelanggan(nama)
        print("  Data penjualan diperbarui.")
    else:
        print("  ! Pilihan tidak valid.")


def cek_status():
    print("  === Status Stok Roti ===")
    for roti in daftar_roti:
        print(f"  {roti.get_kode()} - {roti.get_nama():<20} Stok {roti.get_stok():>3} -> {roti.cek_status()}")
    total = sum(p.hitung_total() for p in daftar_penjualan)
    print(f"  Jumlah transaksi: {len(daftar_penjualan)} | Total pendapatan: Rp{total:,}")


def tampilkan_menu():
    print("\nAPLIKASI PRODUKSI TOKO ROTI")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Cari data")
    print("4. Ubah data")
    print("5. Cek status data")
    print("0. Keluar")


def main():
    aksi = {"1": tambah_data, "2": tampilkan_data, "3": cari_data,
            "4": ubah_data, "5": cek_status}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Terima kasih, program selesai.")
            break
        if pilihan in aksi:
            aksi[pilihan]()
        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()

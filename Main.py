from model.kontak import*

tambah_kontak("Herza", "311910618")
ubah = ubah_kontak("Herza", "08980027530")
if ubah:
    print("Sukses")
else:
    print("gagal")
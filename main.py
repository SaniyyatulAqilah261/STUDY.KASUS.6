import json

with open("data toko.json", "r", encoding = "utf-8") as f:
    data = json.load(f)

def tambah_data (nama, kode, kategori):
    data.append({
        "nama" : nama,
        "kode" : kode,
        "kategori" : kategori
    })

    return "Data ditambah"

def simpan_file():
    with open("data toko.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent = 4)
        return "tersimpan data toko ke data toko.json"

print("=====data awal=====")
print(data)

print("\n",tambah_data("Gula pasir", "C403", "sembako"))

print("\n", simpan_file())

print("==== data setelah ditambah ====")

print (data)

while True:
    print("\n===== MENU DATA TOKO =====")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Simpan Data")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n===== DATA TOKO =====")

        if len(data) == 0:
            print("Belum ada data.")
        else:
            for item in data:
                print("Nama     :", item["nama"])
                print("Kode     :", item["kode"])
                print("Kategori :", item["kategori"])
                print("----------------------")

    elif pilihan == "2":
        nama = input("Masukkan nama barang: ")
        kode = input("Masukkan kode barang: ")
        kategori = input("Masukkan kategori barang: ")

        print(tambah_data(nama, kode, kategori))

    elif pilihan == "3":
        print(simpan_file())

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia.")
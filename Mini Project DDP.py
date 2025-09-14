print("Nama: Zahra Syifa Salsabila")
print("Kelas: B")
print("Tugas: Mini Project DDP")

data_kegiatan = []

print("\nKegiatan Kunjungan PMR ke Panti Asuhan Ruhamaa")

while True:
    print("\nMenu:")
    print("1. Tambah data")
    print("2. Lihat data")
    print("3. Update data")
    print("4. Hapus data")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        kegiatan = input("Masukkan Kegiatan:")
        lokasi = input("Masukkan Lokasi:")
        waktu = input("Masukkan Waktu dan Tanggal:")
        data_kegiatan.append([kegiatan, lokasi, waktu]) 
        print("data berhasil di tambahkan!")

    elif pilihan == "2":
        if len(data_kegiatan) == 0:
            print("data kosong.")
        else:
            for i, kegiatan in enumerate(data_kegiatan, start=1):
                print(f"{i}. Kegiatan: {kegiatan[0]}, Lokasi: {kegiatan[1]}, Waktu dan Tanggal: {kegiatan[2]}")

    elif pilihan == "3":
        if len(data_kegiatan) == 0:
            print("data kosong.")
        else:
            for i, kegiatan in enumerate(data_kegiatan, start=1):
                print(f"{i}. Kegiatan: {kegiatan[0]}, Lokasi: {kegiatan[1]}, Waktu dan Tanggal: {kegiatan[2]}")

        index = int(input("Pilih data yang mau diupdate: ")) - 1
        if 0 <= index < len(data_kegiatan):
            print("Masukkan data baru")
            
            kegiatan_new = input(f"Nama Kegiatan [{data_kegiatan[index][0]}]: ")
            lokasi_new = input(f"Lokasi [{data_kegiatan[index][1]}]: ")
            waktu_new = input(f"Waktu & Tanggal [{data_kegiatan[index][2]}]: ") 

            data_kegiatan[index] = (kegiatan_new, lokasi_new, waktu_new)
            print("data berhasil di update!")
            for i, kegiatan in enumerate(data_kegiatan, start=1):
                print(f"{i}. Kegiatan: {kegiatan[0]}, Lokasi: {kegiatan[1]}, Waktu dan Tanggal: {kegiatan[2]}")

        else:
            print("Nomor tidak valid")

    elif pilihan == "4":
        if len(data_kegiatan) == 0:
            print("data kosong.")
        else:
            for i, kegiatan in enumerate(data_kegiatan, start=1):
                print(f"{i}. Kegiatan: {kegiatan[0]}, Lokasi: {kegiatan[1]}, Waktu dan Tanggal: {kegiatan[2]}")

        index = int(input("Pilih data yang mau di hapus:")) - 1
        if 0 <= index < len(data_kegiatan):
            data_kegiatan.pop(index)
            print("data berhasil di hapus.")
            for i, kegiatan in enumerate(data_kegiatan, start=1):
                print(f"{i}. Kegiatan: {kegiatan[0]}, Lokasi: {kegiatan[1]}, Waktu dan Tanggal: {kegiatan[2]}")
        else:
            print("Nomor tidak valid")

    elif pilihan == "5":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak ada, coba lagi!")
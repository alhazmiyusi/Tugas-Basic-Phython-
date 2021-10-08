list_nama = []
list_nomor = []

while True: 
    print ("-----------------------------")
    print("Selamat datang!")
    print()
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print()
    menu = input("Piih Menu: ")
    print()

    if menu == '2':
        print("Masukkan Data Kontak")
        print ("-----------------------------")
        nama = input("Nama: ")
        nomor = input("No Telepon: ")
        list_nama.append(nama)
        list_nomor.append(nomor)
        print()
        print("Kontak berhasil ditambahkan")

    elif menu == '1': 
        print ("-----------------------------")
        print("Daftar Kontak:")
        print()
        for x in range(len(list_nama)):
            print("Nama = ", list_nama[x])
            print("No.Telepon = ", list_nomor[x])
            print()

    elif menu == '3':
        print ("-----------------------------")
        print("Program selesai, sampai jumpa!")
        break

    else:
        print ("-----------------------------")
        print("Menu tidak tersedia")
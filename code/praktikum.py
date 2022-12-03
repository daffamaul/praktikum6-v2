import os

data_mahasiswa = {}


def tambah():
	os.system("cls")
	print("Tambah Data")
	nama = input("Nama           : ")
	nim = int(input("NIM            : "))
	nilai_tugas = int(input("Nilai Tugas    : "))
	nilai_uts = int(input("Nilai UTS      : "))
	nilai_uas = int(input("Nilai UAS      : "))
	nilai_akhir = nilai_tugas * .3  + nilai_uts * .35 + nilai_uas * .35
	data_mahasiswa[nama] = nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir
def tampilkan():
	os.system("cls")
	if data_mahasiswa.items():
		print("="*84)
		print("|                               Daftar Mahasiswa                                   |")
		print("="*84)
		print("|No. | Nama            |       NIM       |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
		print("="*84)
		i = 0
		for data in data_mahasiswa.items():
			i += 1
			print("| {no:2d} | {0:15s} | {1:15d} | {2:5d}   | {3:^5} |{4:^7}| {5:^13.2f} |".format(data[0], data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], no=i))
		print("=" * 84)
	else:
		os.system("cls")
		print("="*84)
		print("|                               Daftar Mahasiswa                                   |")
		print("="*84)
		print("|No. | Nama            |       NIM       |  Tugas  |  UTS  |  UAS  |  Nilai Akhir  |")
		print("="*84)
		print("|                                TIDAK ADA DATA                                    |")
		print("="*84)

def ubah(nama):
	os.system("cls")
	if nama in data_mahasiswa.keys():
		nim = int(input("NIM            : "))
		nilai_tugas = int(input("Nilai Tugas    : "))
		nilai_uts = int(input("Nilai UTS      : "))
		nilai_uas = int(input("Nilai UAS      : "))
		nilai_akhir = nilai_tugas * .3 + nilai_uts * .35 + nilai_uas * .35
		data_mahasiswa[nama] = nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir
	else:
		print(f"Nama {nama} tidak ditemukan")

def hapus(nama):
	os.system("cls")
	if nama in data_mahasiswa.keys():
	    del data_mahasiswa[nama]
	else:
		print(f"Nama {nama} Tidak Ditemukan")

def cari(nama):
	os.system("cls")
	if nama in data_mahasiswa.keys():
		print("="*84)
		print("|                             Daftar Mahasiswa                                     |")
		print("="*84)
		print("| Nama            |       NIM       |  Tugas  |  UTS  |  UAS  |  Nilai Akhir       |")
		print("="*84)
		print("| {0:15s} | {1:15d} | {2:^7} | {3:^5} | {4:^5} | {5:^18.2f} |".format(nama, *data_mahasiswa[nama]))
		print("="*84)
	else:
		print(f"Nama {nama} Tidak Ditemukan")

while True:
    user = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")

    if user.lower() == 't':
    	tambah()
    elif user.lower() == 'h':
    	nama = input("Masukkan Nama : ")
    	hapus(nama)
    elif user.lower() == 'u':
    	nama = input("Masukkan Nama : ")
    	ubah(nama)
    elif user.lower() == 'l':
    	tampilkan()
    elif user.lower() == 'c':
        nama = input("Masukkan Nama : ")
        cari(nama)
    elif user.lower() == 'k':
    	print("Akhir Program")
    	os.system("cls")
    	break
    else:
    	print("Harap pilih pada menu")


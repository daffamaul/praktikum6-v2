# Flowchart
![Flowchart](/img/function.drawio.png)

# Penjelasan Program

> Mendeklarasikan bahwa variabel _data_mahasiswa_ sebagai penyimpanan (_dictionary_) sebuah data inputan
```python
data_mahasiswa = {}
```

> Perulangan menggunakan _while_ yang bernilai _True_ agar perulangan tersebut terus mengulang dan berakhir menggunakakn sebuah kondisi di dalamnya yang disisipkan metode _break_. 
```python
while True:
   # Syntax Program
```

> Di dalam perulangan terdapat variabel _user_ sebagai penerima inputan yang disimpan ke dalam variabel tersebut
```python
user = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
```
> Jika _user_ value-nya "T", maka akan memanggil sebuah _function_ yang bernama tambah
```python
if user.lower() == 't':
    	tambah()
```
> Pada _function_ **tambah** ini, user diminta untuk menginputkan sebuah data yang di perlukan, data-data yang ditambahkan dibungkus dengan metode _tuple_ (akhir code)
```python
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
```

> Jika _user_ value-nya "h", maka akan memanggil sebuah _function_ yang bernama **hapus**
```python
if user.lower() == 'h':
      nama = input("masukkan nama : ")
      hapus(nama)
```
> Jika nama tersebut ada pada data, maka data tersebut akan di-_delete_ pada _dictionary_ sehingga data tidak tersedia lagi. Jika nama tersebut tidak ada pada data, maka akan menampilkan pesan bahwa nama tidak ditemukan
```python
def hapus(nama):
	os.system("cls")
	if nama in data_mahasiswa.keys():
	    del data_mahasiswa[nama]
	else:
		print(f"Nama {nama} Tidak Ditemukan")
 ```

> Jika _user_ value-nya "u", maka user akan diperintahkan untuk mengisikan inputan nama dan memanggil sebuah _function_ bernama **ubah**
```python
 elif user.lower() == 'u':
    	nama = input("Masukkan Nama : ")
    	ubah(nama)
 ```
 > Jika nama tersebut ada pada data, maka user akan diminta untuk menginputkan data apa saja yang ingin dirubah. Jika nama tersebut tidak ada, maka akan menampilkan bahwa nama tidak ditemukan
 ```python
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
 ```

> Jika user menginputkan "l" atau **lihat**, maka akan memanggil sebuah _function_ bernama **tampilkan**
```python
elif user.lower() == 'l':
    	tampilkan()
```
> Jika sebelumnya data sudah ditambahkan atau data tersedia, maka data tersebut akan ditampilkan sebanyak data yang ditambahkan. Jika data tersebu belum ditambahkan atau tidak tersedia, maka akan menampilkan pesan bahwa tidak ada data
```python
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
```

> Jika user menginputkan 'c' atau **cari**, maka user diharuskan untuk memasukkan nama yang dicari dan selanjutnya program akan memanggil _function_ bernama **cari**
```python
elif user.lower() == 'c':
        nama = input("Masukkan Nama : ")
        cari(nama)
```
> Jika nama tersebut ada pada data, maka akan menampilkan beberapa informasi terkait nama yang dicari. Jika nama tersebut tidak ada pada data, maka akan menampilkan pesan bahwa nama tidak ditemukan
```python
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
```

> Jika user menginputkan 'k' atau maksudnya **keluar**, maka akan menampilkan pesan bahwa ini adalah akhir program dan program akan berhenti dijalankan
```python
elif user.lower() == 'k':
    	print("Akhir Program")
    	os.system("cls")
    	break
```

> Jika user tidak menginputkan sesuatu pada pilihan, maka akan diperintahkan untuk memilih pilihan
```python
else:
    	print("Harap pilih pada menu")
```










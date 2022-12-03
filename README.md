# Flowchart
![Flowchart](/img/function.drawio.png)

# Penjelasan Program
## Main Program
> Mendeklarasikan bahwa variabel _data_mahasiswa_ sebagai penyimpanan (_dictionary_) sebuah data inputan
```python
data_mahasiswa = {}
```

> Perulangan menggunakan _while_ yang bernilai _True_ agar perulangan tersebut terus mengulang dan berakhir menggunakakn sebuah kondisi di dalamnya yang disisipkan metode _break_. 
```python
while True:
   # Syntax Program
```

> Di dalam perulangan terdapat variabel _user_ sebagai menerima inputan yang disimpan ke dalam variabel tersebut
```python
user = input("\n(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar: ")
```
> Jika _user_ value-nya "T", maka baris yang akan dieksekusi akan dikomparasikan dengan inputan tersebut dan jika benar, maka selanjutnya akan di arahkan ke _function_ tambah, pada _function_ tambah akan menghasilkan sebuah _output_ dibawah ini
```python
if user.lower() == 't':
    	tambah()
```
> User diminta menginputkan data sesuai dengan isi
![Tambah](/img/1.png)
> Ketika user ingin melihat datanya, input "l" untuk melihat data untuk melihat apakah data sudah ada pada tabel, jika sudah maka akan tampil sebagai berikut
![Tambah](/img/2.png)
> Jika tidak ada data, maka akan tampil
![Tambah](/img/7.png)

> Jika _user_ value-nya "h", maka baris yang akan dieksekusi akan dikomparasikan dengan inputan tersebut dan jika benar, maka selanjutnya akan di arahkan ke _function_ hapus, sebelum itu, user akan diminta memasukkan nama terlebih dahulu untuk dilakukan pengecekkan, apakah ada nama tersebut pada data atau tidak yang mana itu akan di lakukan pada _function_ hapus yang akan menghasilkan sebuah _output_ dibawah ini
```python
if user.lower() == 'h':
      hapus()
```
> User diminta masukkan nama
![Hapus](/img/6.png)
> Jika nama tersebut ada pada data, maka akan menampilkan tidak adanya sebuah data (karena saya hanya menginputkan satu data saja)
![Hapus](/img/7.png)
> JIka nama tersebut tidak ada, maka akan menampilkan bahwa nama tersebut tidak ada pada data
![Ubah](/img/5.png)

> Jika _user_ value-nya "u", maka baris yang akan dieksekusi akan dikomparasikan dengan inputan tersebut dan jika benar, maka selanjutnya akan di arahkan ke _function_ ubah, sebelum itu, user akan diminta memasukkan nama terlebih dahulu untuk dilakukan pengecekkan, apakah ada nama tersebut pada data atau tidak yang mana itu akan di lakukan pada _function_ ubah
```python
 elif user.lower() == 'u':
    	nama = input("Masukkan Nama : ")
    	ubah(nama)
 ```
> Jika nama tersebut ada pada data, maka user akan diminta input untuk diubah
![Ubah](/img/3.png)
> Jika nama tersebut tidak ada pada data, maka akan menampilkan
![Ubah](/img/5.png)

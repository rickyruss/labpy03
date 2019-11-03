# Algoritma Latihan 1
```
1. Langkah pertama menginputkan penyebut seperti num dan dituliskan int(input("Masukan bilangan: ")) agar kita bisa mengisi bilangan di program tersebut
2. Yang kedua masukan penyebut jumlah = num+1 untuk menambah bilangan yang telah kita isi nanti saat program kita di RUN.
3. Lalu masukan: 
- start = 1 (Untuk memulai hasil program dari satu bukan dari 0.)
- stop = jumlah (Untuk memberhentikan setiap penjumlahan pada num+1.) 
- step = 1 (Untuk menetapkan jumlah yang dipilih dari num = int(input("Masukan bilangan: ")) )
4. Lalu masukan Statment for i in range(start, stop, step): (untuk mengatur jalanya penyebut yg sudah kita buat dri awal)
5. Agar angka yang dimasukan random masukan:
- from random import random
- a = random()
6. Yang terakhir cetaklah variable yang untuk perulangan yang ada pada num: print("Perulangan ke:",i,"=>",(a))
```

## Hasil Screenshot hasil latihan1:
![latihan 1](https://user-images.githubusercontent.com/56240498/68083568-adedcd00-fe5c-11e9-8447-016fa998ce35.png)

# Algoritma Latihan 2
```
1. Langkah pertama yang harus dilakukan mengisi 2 variable yang akan di inputkan bebas:
- bil1 = int()
- bil2 = int()
2. Langkah kedua lansung kita masukan statment:
- while bil1 >= 0:
- bil1 = int(input("Masukan Bilangan: "))
- if bil1 > bil2:
- bil2 = bil1
- if bil1 == 0:
- break
- Pada syntax ini saya akan menjelaskan while bil1 yang akan kita isi lebih dari sama dengan 0,
if atau jika bil1 itu lebih dari bil2,Nah bil2 itu adalah bil1 yang angkanya paling besar pada nantinya.
Variable bil1 akan berhenti jika pada perogram dituliskan angka 0. 
Lalu cetak Variable bil2 Dan program akan otomatis memilih bilangan yg kita masukan paling besar.
```
## Hasil Screenshot hasil latihan2:
![latihan 2](https://user-images.githubusercontent.com/56240498/68083572-bd6d1600-fe5c-11e9-826f-828fb7fa4ca3.png)

# Algoritma Program 1
```python
A. Input 
        modal = 100000000
        laba = 0
        untung = 0 
```
print = Fungsi "print()" berfungsi untuk mencetak atau menampilkan objek ke perangkat keluaran (Layar).Modal itu adalah variable dimana 100000000 adalah modal awal
laba dan untung = adalah variable laba dan variable untung
```python            
  B. Process
      for i in range(1,9,1):
       if(i<3):
        laba = 0
        untung = untung + laba
       elif(i<5):
        laba = modal*1/100
        untung = untung + laba
       elif(i<8):
        laba = modal*5/100
        untung = untung + laba
       else:
        laba = modal*2/100
        untung = untung + laba
      
Penjelasanya adalah = for x in range(1,9,1" = Perulangan i dengan nilai pertama 1, nilai terakhir 9 dan step 1)
Lalu if = Bila suatu kondisi tertentu tercapai maka apa yang harus dilakukan. Dengan fungsi ini kita bisa menjalankan suatu perintah dalam kondisi tertentu. 
elif = Dan Jika kondisi lainnya berbeda maka jalankan program.
else = Selain tidak ada suatu kondisi yang terpenuhi maka jalankan program
for = Untuk perulangan yang terhitung.
range = Mengembalikan deret integer berurut pada Jarak yang ditentukan dari start sampai stop.
```
```python        
   C.Hasil Run
      print("Laba Bulan Ke-",i," Sebesar ",laba)
      Cetak laba per bulan
    print("\nTotal Laba adalah: ",untung)
      Cetak total laba
```
## Hasil Screenshot Program 1
![program 1](https://user-images.githubusercontent.com/56240498/68083573-c1009d00-fe5c-11e9-86da-5a4a8d92f2ae.png)

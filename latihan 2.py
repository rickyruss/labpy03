#Program untuk menampilkan bilangan terbesar dari hasil inputan,Masukan angka 0 untuk berhenti.
bil1 = int()
bil2 = int()
while bil1 >= 0:
    bil1 = int(input("Masukan Bilangan: "))
    if bil1 > bil2:
        bil2 = bil1
    if bil1 == 0:
        break
print("Angka terbesar adalah: ",bil2)
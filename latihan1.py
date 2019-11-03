#Menampilkan Bilangan acak lebih kecil dari 0.5
num = int(input("Masukan bilangan: "))
jumlah = num+1
start = 1
stop = jumlah
step = 1
for i in range(start, stop, step):
    from random import random
    a = random()
    print("Perulangan ke:",i,"=>",(a))
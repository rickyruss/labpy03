#Program Sederhana dengan perulangan dengan soal cerita pada modul Praktikum 3
modal = 100000000
untung = 0
laba = 0
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
 print("Laba Bulan Ke- ",i," Sebesar ",laba)
print("Total Laba adalah: ",untung) 

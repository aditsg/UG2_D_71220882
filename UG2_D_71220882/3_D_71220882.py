namabrand = input("Masukan brand apa saja yang hendak dibeli (pisahkan dengan koma) : ")

hargabrand = input("Berapa harga barang H&M ? : ")
print("Harga H&M   Rp. ", hargabrand,"Diskon Rp. ")

hargabrand1 = (input("Berapa harga barang Fendi ? : "))
print("Harga Fendi   Rp. ", hargabrand1,"Diskon Rp. ",rs)

hargabrand2 = int(input("Berapa harga barang LV ? : "))
print("Harga LV  Rp. ", hargabrand2,"Diskon Rp. ", rd)

hargabrand3 = int(input("Berapa harga barang Dior ? : "))
print("Harga Dior  Rp. ", hargabrand3,"Diskon Rp. ", rf)

rs =  hargabrand1 / 100 * 25
rd =  hargabrand2 / 100 * 10 
rf =  hargabrand3 / 100 * 25 
total1 = hargabrand + hargabrand1 + hargabrand2 + hargabrand3
total =  rs + rd + rf
totaldiskon = total1 - total 
print("Total diskon yang anda dapatkan Rp. ", totaldiskon)
print("Total uang yang harus dibayarkan adalah Rp. ",total)

print("  !! Selamat Datang Di H+ GYM !!  ")
print("Silahkan pilih menu dibawah ini : ")
print("1. Menambah Data ")
print("2. Menampilkan data")
print("3. Keluar")

msk = int(input("Silakan masukan pilihan yang anda inginkan : "))

while msk== 1 : 
    plg = input("masukan nama pelanggan : ")
    mbr = input("masukan jenis member : ")
    print("data sudah berhasil ditambahkan!")
    msk = int(input("Silakan masukan pilihan yang anda inginkan : "))
    
if msk== 2 :
    print("Pelanggan : ",plg)
    print("Member : ", mbr)
    msk = int(input("Silakan masukan pilihan yang anda inginkan : "))
if msk== 3 : 
    print("Sistem berhenti........")



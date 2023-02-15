print("============ MAKANAN ===========")
telur = int(input("1. Telur Bakar            : Rp " ))
lele = int(input("2. Lele Terbang Mas Bhe   : Rp "))
coklat = int(input("3. Es Coklat Lempu        : Rp "))
doger = int(input("4. Es Doger Langensari    : Rp "))

print("============ PESANAN ===========")
bakar = int(input("Telur Bakar        :"))
terbang = int(input("Lele terbang       :"))
lempu = int(input("Es Coklat          :"))
sari =  int(input("Es Doger           :"))

rumus1 = telur * bakar 
rumus2 = lele * terbang 
rumus3 = coklat * lempu
rumus4 = doger * sari

print("============ TOTAL ===========")
print("Toatal telur bakar X ",bakar,"     :",rumus1)
print("Total lele terbang X",terbang,"      :",rumus2)
print("Total es coklat X", lempu,"         :",rumus3)
print("Total es doger X", sari,"          :",rumus3)

rumus5 = rumus1 + rumus2 + rumus3 + rumus4

print("Jumlah total biaya yang harus dibayar adalah Rp.",rumus5 )


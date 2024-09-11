data1 = int(input("masukkan angka pertama: "))
data2 = int(input("masukkan angka kedua: "))
data3 = int(input("masukkan angka ketiga: "))

if data1 >= data2 and data1 >= data3:
    print("lebih besar data ", data1)
elif data2 >= data1 and data2 >= data3:
    print("lebih besar data ", data2)
else:
    print("lebih besar data ", data3)
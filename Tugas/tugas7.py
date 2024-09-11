nilai = int(input("masukkan nilai: "))

if nilai >= 85 and 100:
    print("nilai anda A")
elif nilai >= 70 and 84:
    print("nilai anda B")
elif nilai >= 55 and 69:
    print("nilai anda C")
elif nilai >= 40 and 54:
    print("nilai anda D")
else:
    print("nilai anda E")
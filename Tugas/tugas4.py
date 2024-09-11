dataUmur = int(input("masukkan umur anda: "))

if dataUmur < 12:
    print("anda masih anak anak")
elif dataUmur < 18:
    print("anda udah remaja")
elif dataUmur >= 18:
    print("anda udah dewasa")
else:
    print("program selesai")
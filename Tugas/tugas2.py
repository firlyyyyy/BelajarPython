# --------0+++++++5---------8+++++++11--------

inputData = float(input("masukkan nilai: "))

angka1 = inputData >= 0 and inputData <= 5
print("angka pertama: ", angka1)

angka2 = inputData >= 8 and inputData <= 11
print("angka kedua: ", angka2)

hasil = angka1 or angka2
print("hasil: ", hasil)

# ++++++++0-------5+++++++++8-------11++++++++

inputData = float(input("masukkan nilai: "))

angka1 = inputData <= 0 or inputData >= 5
print("angka pertama: ", angka1)

angka2 = inputData <= 8 or inputData >= 11
print("angka kedua: ", angka2)

hasil = angka1 and angka2
print("hasil: ", hasil)
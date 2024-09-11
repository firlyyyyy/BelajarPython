# perulangan (loop)

# for kondisi:
#     aksi

# menggunakan list
angkaList = [0, 1, 2, 3]  # ini adalah list

for i in angkaList:
    print(i)
print("list end")

# menggunakan range
angkaRange = range(5)

for i in angkaRange:
    print(i)
print("rangge end")

# while loop

# while kondisi:
#     aksi

angka = 0
print("angka ->", angka)

while angka < 5:
    angka += 1
    print("angka ->", angka)
    print("helo")
print("while end")
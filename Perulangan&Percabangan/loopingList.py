# looping list

# menggunakan for loop
p = "FOR LOOP".ljust(35, "-")
print(p)
kumpulan_angka = [1, 2, 3, 4, 5]

for angka in kumpulan_angka:
    print(f"angka - {angka}")
    
kumpulanNama = ['udin', 'ucup', 'ilham']

for nama in kumpulanNama:
    print(f"nama: {nama}")
    
print("\n")

# menggunakan for loop dan range
p = "FOR LOOP DAN RANGE".ljust(35, "-")
print(p)
kumpulan_angka = [5, 4, 3, 2, 1]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

print("\n")

# menggunakan while
p = "WHILE".ljust(35, "-")
print(p)
kumpulan_angka = [5, 4, 3, 2, 1]
panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

print("\n")    
# list comprehension
p = "LIST COMPREHENSION".ljust(35, "-")
print(p)
data = ['a', 'b', 'c']

[print(f"data = {i}") for i in data]  # cara menggunakan list comprhension

angka = [2, 5, 7, 2]
angkaKuadrat = [i**2 for i in angka]
print(f"kuadrat = {angkaKuadrat}")
print("\n")

# enumerate
p = "ENUMERATE".ljust(35, "-")
print(p)
dataList = ['z', 'x', 'y']

for index, data in enumerate(dataList):
    print(f"index = {index}, data = {data}")
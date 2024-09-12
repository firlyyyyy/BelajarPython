# looping dictionary

namaOrang = {
    "ris": "riski",
    "yus": "yusuf",
    "bdi": "budi",
}

# looping first try (yang keluar adalah key nya)
for nama in namaOrang:
    print(f"nama :  {nama}")
print("\n")

# operator untuk mengambil item / iterables

# keys
keys = namaOrang.keys()  # digunakan untuk mengambil key
print(keys)

for key in namaOrang.keys():
    print(namaOrang.get(key))
print("\n")

# values
values = namaOrang.values()  # digunakan untuk mengambil value
print(values)

for value in namaOrang.values():
    print(f"nama : {value}")
print("\n")

# items
items = namaOrang.items()  # digunakan untuk mengambil key dan value
print(items)

for item in namaOrang.items():  # item adalah tuple
    print(item)

for key, value in namaOrang.items():  # digunakan untuk mengambil key dan value secara bersamaan
    print(f"key : {key}, value : {value}")

# copy dictionary

teman = {
    "nama1": "ahmad",
    "nama2": "budi",
    "nama3": "caca",
    "nama4": "dina",
}

temanCopy = teman
teman.update({"nama1": "udin"})
print(f"address teman {hex(id(teman))} | \n{teman}")
print(f"address teman copy {hex(id(temanCopy))} | \n{temanCopy}")
print("\n")

temanCopy = teman.copy()  # digunakan untuk membuat salinan dari dictionary
teman.update({"nama1": "ahmad"})
print(f"address teman {hex(id(teman))} | \n{teman}")
print(f"address teman copy {hex(id(temanCopy))} | \n{temanCopy}")
print("\n")

# pop dictionary di ambil dari key
data1 = temanCopy.pop("nama1")  # pop() --> digunakan untuk mengambil satu item dari dictionary
print(f"data 1 = {data1}")
print(f"teman copy = {temanCopy}")
print("\n")

# popitem dictionary yang di ambil dari item terakhir
data4 = temanCopy.popitem()  # digunakan untuk mengambi data terakhir dari dictionary
print(f"data 4 = {data4}")
print(f"teman copy = {temanCopy}")
# print("\n")
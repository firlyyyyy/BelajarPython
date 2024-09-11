# operasi pada list

data = ["a", "b", "c"]
# mengambil data list menggunakan index
print(f"nilai index 0 = {data[0]}")
print(f"nilai index 1 = {data[1]}")
print(f"nilai index 2 = {data[2]}")

# mengamil info jumlah data dalam list
panjang_data = len(data)  # len() --> untuk mengetahui jumlah data yang ada di list
print(f"panjang data = {panjang_data}")

# manipulasi data list

# menambah item pada list sesuai posisi
print(f"data sebelum {data}")

# data.insert(posisi, item)
data.insert(3, "d")
print(f"data sesudah {data}")
data.insert(0, "e")
print(f"data sesudah {data}")
data.append("u")
print(f"append {data}")

# menambahkan list dengan list
data_baru = ["x", "y", "z"]
print(f"data sebelum di extend {data}")
data.extend(data_baru)  # extend() --> untuk menggabungkan data baru
print(f"data sesudadh di extend {data}")

# mengubah data list
print(f"data sebelum di ubah {data}")
data[4] = "R"  # untuk merubah data
print(f"data sesudah di ubah {data}")

# menghapus data list
print(f"data sebelum di hapus {data}")
data.remove("z")  # untuk menghapus data
print(f"data sesudah di hapus {data}")
data.pop()  # pop() --> digunakan untuk menghapus data paling akhir
print(f"menghapus data paling akhir {data}")
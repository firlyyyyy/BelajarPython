# operasi list

data_angka = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5]
print(f"data angka = {data_angka}")

# count data
jumlahData1 = data_angka.count(1)  # count() --> digunakan untuk menghitung berapa jumlah data
jumlahData2 = data_angka.count(2)
jumlahData3 = data_angka.count(3)
jumlahData4 = data_angka.count(4)
jumlahData5 = data_angka.count(5)
print(f""" 
jumlah data 1 = {jumlahData1}
jumlah data 2 = {jumlahData2}
jumlah data 3 = {jumlahData3}
jumlah data 4 = {jumlahData4}
jumlah data 5 = {jumlahData5}\n""")

# ambil posisi data
data = ["z", "g", "b", "u", "s"]
dataIndex = data.index("u")
print(f"data u berindex = {dataIndex}\n")

# mengurutkan list
print(f"data angka sebelum sort = {data_angka}")
data_angka.sort()
print(f"data angka sesudah sort = {data_angka}\n")

print(f"data huruf sebelum sort = {data}")
data.sort()
print(f"data huruf sesudah sort = {data}\n")

# reverse data
print(f"data angka sebelum di reverse = {data_angka}")
data_angka.reverse()
print(f"data angka sesudah di reverse = {data_angka}\n")

print(f"data huruf sebelum di reverse = {data}")
data.reverse()
print(f"data huruf sesudah di reverse = {data}")

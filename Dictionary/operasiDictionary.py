# operator dictionary

data_dict = {
    "a": "abc",
    "b": "bca",
    "c": "cba",
}

# panjang dictionary
# digunakan  untuk menghitung jumlah item dalam dictionary
LENDICT = len(data_dict)
print(f"panjang  dictionary : {LENDICT}")

# mengecek  apakah key ada di dictionary
KEY = "a"
KEYCHEK = KEY in data_dict  # digunakan  untuk mengecek apakah key ada di dictionary
print(f"apakah  key {KEY} ada di dictionary : {KEYCHEK}")

# mengakses value dari key menggunakan get
# digunakan   untuk mengakses value dari key
print(f"data a : {data_dict.get("a")}")
# cek apakah key ada di dictionary jika tidak ada maka akan menampilkan data tidak ditemukan
print(f"data v : {data_dict.get("v", "data tidak ditemukan")}")

# update value dari key
data_dict["a"] = "zxc"  # digunakan  untuk update value dari key
print(data_dict)

# menambah kan key baru
data_dict["d"] = "xbd"  # digunakan  untuk menambahkan key baru
print(data_dict)

data_dict.update({"a": "abc"})  # digunakan  untuk menambahkan key baru
print(data_dict)

# digunakan  untuk menambahkan key baru, jika  key sudah ada maka akan mengupdate value
data_dict.update({"e": "yui"})
print(data_dict)

# hapus data dari dictionary
del data_dict["d"]  # digunakan  untuk menghapus data dari dictionary
print(data_dict)

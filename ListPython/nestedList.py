# nested list --> list di dalam list

data0 = [1, 2]
data1 = [3, 4, 5]
listBiasa = [1, 2, 3, 4, 5]

print(f"""
data 0 = {data0}
data 1 = {data1}
list biasa = {listBiasa}\n""")

# menggabungkan data0 dan data1
dataGabung = [data0, data1]
print(f"data gabung 0 dan 1 = {dataGabung}\n")

# contoh penggunaan
peserta1 = ["udin", 20, "laki-laki"]
peserta2 = ["ucup", 19, "laki-laki"]
peserta3 = ["usil", 18, "perempuan"]

listPeserta = [peserta1, peserta2, peserta3]

print(f"peserta = {listPeserta}\n")

p = "PESERTA".ljust(25, "-")
print(p, "\n")
for peserta in listPeserta:
    print(f"nama peserta\t: {peserta[0]}")
    print(f"umur peserta\t: {peserta[1]}")
    print(f"kelamin peserta\t: {peserta[2]}\n")
    
p = "GAME".ljust(25, "-")
print(p, "\n")
game1 = ["PUBG", "shooter"]
game2 = ["FORNITE", "shooter"]
game3 = ["MINECRAFT", "adventure"]
game4 = ["ROBLOX", "adventure"]
game5 = ["MOBILE LEGEND", "moba"]

listGame = [game1, game2, game3, game4, game5]

for game in listGame:
    print(f"name\t: {game[0]}")
    print(f"genre\t: {game[1]}\n")
    
# mengabil data nested list
a = [1, 2]
b = [3, 4]
c = [a, b, 10]
c_copy = c.copy()
print(f"c = {c}")

data = c[0][0]  # kurung yang pertama di gunakan untuk mengambil data yang pertama yaitu data a, kurung yang kedua digunakan untuk mengambil data yang berada di dalam data a
print(f"data = {data}\n")

# address
print(f"address data c \t\t= {hex(id(c))}")
print(f"address data c copy \t= {hex(id(c_copy))}\n")

print("address dari data ke 1")
print(f"address data c \t\t= {hex(id(c[0]))}")
print(f"address data c copy \t= {hex(id(c_copy[0]))}\n")

c[0][0] = 5
c[2] = 5
print(f"data c \t\t= {c}")
print(f"data c copy \t= {c_copy}\n")

# deep copy nested list
from copy import deepcopy  # cara menggunakan deep copy, harus di import, cara penggunannya

c = [a, b, 10]
c_deepcopy = deepcopy(c)

print(f"address c \t\t= {hex(id(c))}")
print(f"address c deepcopy \t= {hex(id(c_deepcopy))}\n")

c[0][0] = 10
c[0][1] = 20
print(f"data c \t\t= {c}")
print(f"data c deepcopy = {c_deepcopy}\n")
print("address dari data ke 1")
print(f"address data c \t\t= {hex(id(c[1]))}")
print(f"address data c copy \t= {hex(id(c_deepcopy[1]))}\n")

c[1][0] = 40
print(f"data c \t\t= {c}")
print(f"data c copy \t= {c_copy}")
print(f"data c deepcopy = {c_deepcopy}")
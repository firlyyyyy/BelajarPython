# default argumen

# def fungsi(argumen)
# def fungsi(argumen = nilai default)

# argumen biasa
def hai(nama):
    print(f"hai {nama}")
    
hai("udin")

# default argumen
def helo(nama = "ucup"):
    return f"helooo {nama}"

hai = helo()
print(hai)

def tambah(angka1 = 10, angka2 = 10):
    hasil = angka1 + angka2
    return hasil

print(tambah(angka1 = 40))

def kabar(nama, pesan = f"apakabarrr???"):
    return print(f"haii {nama} {pesan}")

kabar(
    input("nama: ")
)
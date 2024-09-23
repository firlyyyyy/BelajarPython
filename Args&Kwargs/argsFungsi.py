""" *args pada fungsi """
# *args adalah sebuah fungsi yang dapat menerima argumen yang tidak terbatas

""" *args """
def fungsi(*args):
    nama = args[0]
    berat = args[1]
    tinggi = args[2]
    print(f"nama {nama} berat {berat} tinggi {tinggi}")
    
fungsi(
    input("nama: "),
    int(input("berat: ")),
    int(input("tinggi: ")),
)

def tambah(*data):
    """ data tipenya tuple, dan dia bisa diiterasi """
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(10, 10, 5)
print(f"hasil = {hasil}")
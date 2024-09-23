""" **kwargs pada fungsi"""
# **kwargs adalah singkatan dari keyword arguments, yang berarti kita bisa mengirimkan argumen dengan nama yang kita inginkan

def fungsiBiasa(nama, berat, tinggi):
    """ Fungsi Biasa """
    print(f"nama {nama}, berat {berat}, tinggi {tinggi}")


fungsiBiasa("udin", 100, 200)


def fungsiKwargs(**kwargs):
    """ Fungsi Kwargs """
    print(kwargs["berat"])


fungsiKwargs(nama="ucup",  berat=100, tinggi=200)

""" studi kasus """

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("opsi tidak tersedia")
        
    return output
        
hasil = math(10, 2, 2, option="tambah")
print(f"hasil penjumlahan = {hasil}")
hasil = math(10, 10, option="kali")
print(f"hasil perkalian = {hasil}")
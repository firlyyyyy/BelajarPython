# __main__  adalah top level code environment

# __name__ == "__main__" --> akan terjadi jika ada di program utama

# __name__ --> pada file program utama
import __fungsi__
print(f"nilai dari file __main__.py = {__name__}")

# import file external

# contoh penggunaan __main__

# deklarasi


def fungsi_tambah(a: int, b: int) -> int:
    return a + b


# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 5
    hasil = fungsi_tambah(angka1, angka2)
    print(f"hasil dari {angka1} + {angka2} = {hasil}")
    
# import package
import mainPackage
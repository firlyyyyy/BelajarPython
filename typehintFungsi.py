""" Type Hints Fungsi """

# type hints adalah cara untuk menambahkan informasi tentang tipe data yang akan dikembalikan oleh fungsi
def biodata(nama:str, umur:int):
    """ Fungsi biodata untuk menampilkan biodata seseorang """
    print(f"Nama : {nama}")
    print(f"Umur : {umur} tahun")
    return nama, umur

biodata(
    input("masukkan nama: "),
    int(input("masukkan umur: "))
)
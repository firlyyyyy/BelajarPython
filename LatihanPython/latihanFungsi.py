"""latihan fungsi"""

import os

# header
def header():
    """Fungsi Header"""
    os.system("clear")
    print(f"{'MENGHITUNG LUAS':^40}")
    print(f"{'DAN':^40}")
    print(f"{'KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")
    
# input user
def input_user():
    """Fungsi Input User"""
    lebar = int(input("masukkan panjang: "))
    panjang = int(input("masukkan lebar: "))
    return lebar, panjang
    
# rumus luas
def luas(panjang, lebar):
    """Fungsi Rumus Luas"""
    return panjang * lebar

def keliling(panjang, lebar):
    return 2 * (panjang + lebar)

# program utama
while True:
    header()
    opsi = input("1. menghitung luas\n2. menghitung keliling\npilih (1 / 2): ")
    
    if opsi == "1":
        LEBAR, PANJANG = input_user()
        LUAS = luas(PANJANG, LEBAR)
        print(f"hasil perhitugan luas = {LUAS}")
        
    elif opsi == "2":
        LEBAR, PANJANG = input_user()
        KELILING = keliling(PANJANG, LEBAR)
        print(f"hasil perhitungan keliling = {KELILING}")
        
    isLanjut = input("apakah ingin lanjut menghitung? (y / n): ")
    if isLanjut == "n":
        break

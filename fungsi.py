'''
    fungsi --> (1. function, 2. method, 3. subrutin/rutin
'''
# membuat fungsi
import os

def hello(sisi):
    sisi = 9
    count = 1
    spasi = int(sisi / 2)

    while True:
        if (count % 2):
            print(" " * spasi + "*" * count)
            count += 1
            spasi -= 1
        else:
            count += 1
            continue

        if count > sisi:
            break

    spasi = 1
    count = sisi - 2

    while True:
        if (count % 2):
            print(" " * spasi + "*" * count)
            spasi += 1
            count -= 1
        else:
            count -= 1
            continue

        if count <= 0:
            break

# hello()

# fungsi dengan argumen

    """def nama_fungsi(argumen):
           badan_fungsi
    """


def hello(nama, kelas, jurusan):
    """_summary_

    Args:
        nama (_type_): _description_
    """
    print(f"nama {nama}, kamu kelas {kelas}, jurusan {jurusan}")

# hello(
#     input("masukkan nama anda: "),
#     input("masukkan kelas: "),
#     input("masukkan jurusan: ")
# )


def kalkulator(angka1, operator, angka2,):
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    
    print(f"hasi dari {angka1} {operator} {angka2} = {hasil}")

def judul():
    print("="*20)
    print(f"{"KALKULATOR SEDERHANA":^10}")
    print("="*20)

os.system("clear")
judul(),

kalkulator(
    int(float(input("masukkan angka 1: "))),
    input("masukkan operator (+, -, *, /): "),
    int(float(input("masukkan angka 2: ")))
)

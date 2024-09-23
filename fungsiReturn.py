# fungsi dengan return

# template fungsi dengan return
# def nama_fungsi(argumen):
#     badan_fungsi
#     return outpur

def kuadrat(input):
    hasil = input**2
    return hasil

print(kuadrat(int(input("masukkan angka: "))))
print("\n")

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    return f"hasil dari {angka1} + {angka2} = {hasil}"
print(tambah(
    int(input("masukkan angka 1: ")),
    int(input("masukkan angka 2: ")),
))
print("\n")

def kalkulator(angka1, operator, angka2):
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        print("operasi tidak ditemukan")
        
    return f"hasil dari {angka1} {operator} {angka2} = {hasil}"

print(kalkulator(
    int(float(input("masukkan angka pertama: "))),
    input("masukkan operator (+,-,*,/): "),
    int(float(input("masukkan angka kedua: "))),
))
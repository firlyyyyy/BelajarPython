# latihan kalkulator sederhana

p = "KALKULATOR SEDERHANA".center(40, "-")
print(p)

angkaPertama = float(input("masukkan angka pertama = "))
operator = input("masukkan operator (+,-,*,/) = ")
angkaKedua = float(input("masukkan angka kedua = "))

if operator == "+":
    hasil = angkaPertama + angkaKedua
    print("hasil dari", angkaPertama, operator, angkaKedua, "=", hasil)
elif operator == "-":
    hasil = angkaPertama - angkaKedua
    print("hasil dari", angkaPertama, operator, angkaKedua, "=", hasil)
elif operator == "*":
    hasil = angkaPertama * angkaKedua
    print("hasil dari", angkaPertama, operator, angkaKedua, "=", hasil)
elif operator == "/":
    hasil = angkaPertama / angkaKedua
    print("hasil dari", angkaPertama, operator, angkaKedua, "=", hasil)
else:
    print("operator tidak ditemukan")
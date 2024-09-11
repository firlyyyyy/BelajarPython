nilai1 = float(input("masukkan nilai pertama: "))
operator = input("masukkan oprator (+,-,*,/): ")
nilai2 = float(input("masukkan nilai kedua: "))

if operator == "+":
    hasil = nilai1 + nilai2
    print(f"hasil dari {nilai1} + {nilai2} = {int(hasil)}")
elif operator == "-":
    hasil = nilai1 - nilai2
    print(f"hasil dari {nilai1} - {nilai2} = {int(hasil)}")
elif operator == "*":
    hasil = nilai1 * nilai2
    print(f"hasil dari {nilai1} * {nilai2} = {int(hasil)}")
elif operator == "/":
    hasil = nilai1 / nilai2
    print(f"hasil dari {nilai1} / {nilai2} = {int(hasil)}")
else:
    print("operator tidak ditemukan")
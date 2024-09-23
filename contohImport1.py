while True:
    def kalkulator(angka1, operator, angka2):
        if operator == "+":
            hasil =  angka1 + angka2
            print(f"{angka1} {operator} {angka2} = {hasil}")
        elif operator == "-":
            hasil = angka1 - angka2
            print(f"{angka1} {operator} {angka2} = {hasil}")
        elif operator == "*":
            hasil = angka1 * angka2
            print(f"{angka1} {operator} {angka2} = {hasil}")
        elif  operator == "/":
            hasil = angka1 / angka2
            print(f"{angka1} {operator} {angka2} = {hasil}")
        else:
            hasil = "Operator tidak dikenal"

    kalkulator(
        angka1 = int(float(input("masukkan angka pertama: "))),
        operator = input("masukkan operator  (+, -, *, /): "),
        angka2 = int(float(input("masukkan angka kedua: "))),
    )
    
    lanjut = input("apakah ingin lanjut? (y / n) ")
    if lanjut == "n":
        break
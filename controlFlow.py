# continue, pass, break

# pass --> berfungsi sebagai dummy, tidak akan di eksekusi

# angka = 0

# while angka < 3:
#     angka += 1 
    
#     if angka == 2:
#         pass  # tidak akan di eksekusi
    
#     print(angka)
# print("end")

# continue
angka = 0
print("angka ->", angka)

while angka < 5:
    angka += 1
    print("angka ->", angka)
    
    if angka == 3:
        print("helo")
        continue  # akan membuat loop meloncat ke step selanjutnya
    
    print("hai")
print("end \n")

# break
input = int(input("masukkan angka: "))

angka = 0
print("angka ->", angka)

while True:
    angka += 1
    print("angka ->", angka)
    
    if angka == input:
        break  # akan membuat loop berhenti di angka yang kita input
    
    # print("hello world")
print("end")

angka = 0
print("angka ->", angka)

while angka < 3:
    angka += 1
    print("angka ->", angka)
    
print("end")
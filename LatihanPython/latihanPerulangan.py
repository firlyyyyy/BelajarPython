# latihan perulangan

# menggunakan for
p = "FOR".center(35, "-")
print(p)
sisi = 13
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1

print(p)
print("\n")

# menggunakan while
p = "WHILE".center(35, "-")
print(p)
count = 1
while True:
    print("*"*count)
    count += 1
    if count > sisi:
        break
    
print(p)
print("\n")

# hanya ganjil saja
p = "GANJIL SAJA".center(35, "-")
print(p)
count = 1
while True:
    if (count % 2):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
    
    if count > sisi:
        break
    
print(p)
print("\n")

# segitiga sama sisi
p = "SEGITIGA SAMA SISI".center(35, "-")
print(p)
count = 1
spasi = int(sisi / 2)
while True:
    if (count % 2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    
    if count > sisi:
        break
    
while True:
    if (count % 2):
        spasi += 1
        print(" "*spasi, "+"*count)
        count -= 1
    else:
        count -= 1
        
    if count > sisi:
        break
    
print(p)
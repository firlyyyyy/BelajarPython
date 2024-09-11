p = "KETUPAT".center(35, "-")
print(p)

sisi = 7
count = 1
spasi = int(sisi / 2)

while True:
    if (count % 2):
        print(" " * spasi + "I" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    
    if count > sisi:
        break
    
count = sisi - 2
spasi = 1

while True:
    if (count % 2):
        print(" " * spasi + "I" * count)
        spasi += 1
        count -= 1
    else:
        count -= 1
        continue
    
    if count <= 0:
        break
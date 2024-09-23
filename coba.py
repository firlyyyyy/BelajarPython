def segitiga(sisi):
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
    
    return sisi

segitiga(
    int(input("masukkan sisi: "))
)
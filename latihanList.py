# proram list buku
p = 'MASUKKAN DATA BUKU'.ljust(35, "-")
print(p)

listBuku = []
while True:
    judul = input("judul bulu\t: ")
    penulis = input("penulis buku\t: ")

    dataBuku = [judul, penulis]
    listBuku.append(dataBuku)
    
    print("No.\t | Judul\t | Penulis")
    for index, buku in enumerate(listBuku):
        print(f"{index+1}.\t | {dataBuku[0]}\t\t | {dataBuku[1]}")
        
    print("\n")
    isStop = input("apakah ingin di lanjur?(y/n) ")
    
    if isStop == "y":
        continue
    elif isStop == "n":
        break
    else:
        print("selesai menambah buku")
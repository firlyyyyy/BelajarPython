# write digunakan untuk menulis ke file, dan jika belum ada file maka akan dibuat
with open("WriteFileExternal/data_1.txt", mode="w", encoding="utf-8") as file:
    file.write("hello world\n")
    file.write("Muhammad Firly Al Faridzi\n")
    file.write("Dinda Ratu Aqifah")
    print(f"status write: {file.writable()}")
    
with open("WriteFileExternal/data_1.txt", mode="r") as file:
    print(file.read())
    print(f"status read: {file.readable()}")
    
## bisa menggunakan append, yang berfungsi untuk menambahkan data ke file yang sudah ada

with open("WriteFileExternal/data_2.txt", mode="w", encoding="utf-8") as file:
    file.write("hello world\n")
    
with open("WriteFileExternal/data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("halloooo\n")
    
with open("WriteFileExternal/data_2.txt", mode="a", encoding="utf-8") as file:
    file.write("haiiiiii\n")
    
## menggunakan r+
# with open("WriteFileExternal/data_3.txt", mode="w", encoding="utf-8") as file:
#     file.write("hello world\n")
    
# with open("WriteFileExternal/data_3.txt", mode="r+") as file:
#     content = file.read()
#     print(content)
#     file.write("haiii\n")
#     file.write("heloooooo\n")
#     file.write("hohohohohohohoh\n")
#     file.write("ihihihihihihihihih")
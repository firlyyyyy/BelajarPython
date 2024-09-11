# membuat gabungan rentan angka

inputUser = int(input("masukkan angka < 3 atau > 10 : "))

# memeriksa angka < 3
print("=== KURANG DARI ===")
isKurangDari = inputUser < 3
print(inputUser, "<", "3", isKurangDari)

# memeriksa angka > 10
print("=== LEBIH DARI ===")
isLebihDari = inputUser > 10
print(inputUser, ">", "10", isLebihDari)

# membadingkan angka
# ++++++++++3-------------10++++++++++++++
isCorrect = isKurangDari or isLebihDari
print("nilai yang dimasukkan : ", isCorrect)

# -----------3++++++++++++10---------------
# kasus irisan
inputUser = int(input("masukkan angka > 3 atau < 10 : "))

# -----------3+++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("lebih dari 3 : ", isLebihDari)

# ++++++++++10-------------
# kurang dari 10
isKurangDari = inputUser < 10
print("kurang dari 10 : ", isKurangDari)

# -----------3++++++++++++10---------------
isCorrect = isKurangDari and isLebihDari
print("nilai yang dimasukkan : ", isCorrect)
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("800x1000")
window.resizable(False, False)
window.title("Kalkulator Sederhana")

# judul
judul = tk.Label(window, text="Kalkulator Sederhana", font=("Arial", 24, "bold"), bg="white")
judul.pack(pady=20)

# variable dan fungsi
ANGKA_PERTAMA = tk.StringVar()
OPERATOR = tk.StringVar()
ANGKA_KEDUA = tk.StringVar()


def hitung():
    angka_pertama = int(float(ANGKA_PERTAMA.get()))
    operator = OPERATOR.get()
    angka_kedua = int(float(ANGKA_KEDUA.get()))
    
    if operator == "+":
        hasil = angka_pertama + angka_kedua
    elif operator == "-":
        hasil = angka_pertama - angka_kedua
    elif operator == "*":
        hasil = angka_pertama * angka_kedua
    elif operator == "/":
        if angka_kedua != 0:
            hasil = angka_pertama / angka_kedua
        else:
            showinfo(title="Error", message="tidak bisa membagi dengan nol")
            return
    else:
        showinfo(title="Error", message="operator tidak valid")
        return
        
    pesan = f"hasil {angka_pertama} {operator} {angka_kedua} = {hasil}"
    showinfo(title="Hasil", message=pesan)
        
# frame input
input_frame = ttk.Frame(window)
input_frame.pack(padx=40, pady=15, fill="x", expand=True)

# komponen

# 1. angka pertama
angka_pertama = ttk.Label(input_frame, text="Angka Pertama")
angka_pertama.pack(padx=40, pady=15, fill="x", expand=True)
angka_pertama_entry = ttk.Entry(input_frame, textvariable=ANGKA_PERTAMA)
angka_pertama_entry.pack(padx=40, pady=15, fill="x", expand=True)

# 2. operator
operator = ttk.Label(input_frame, text="Operator (+,-,*,/)")
operator.pack(padx=40, pady=15, fill="x", expand=True)
operator_entry = ttk.Entry(input_frame, textvariable=OPERATOR)
operator_entry.pack(padx=40, pady=15, fill="x", expand=True)

# 3. angka kedua
angka_kedua = ttk.Label(input_frame, text="Angka Kedua")
angka_kedua.pack(padx=40, pady=15, fill="x", expand=True)
angka_kedua_entry = ttk.Entry(input_frame, textvariable=ANGKA_KEDUA)
angka_kedua_entry.pack(padx=40, pady=15, fill="x", expand=True)

# tombol hasil
hasil_tombol = ttk.Button(input_frame, text="Hasil", command=hitung)
hasil_tombol.pack(padx=40, pady=15, fill="x", expand=True)
window.mainloop()

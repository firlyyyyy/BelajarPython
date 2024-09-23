""" TKINTER GUI (Graphical User Interface) """

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(
    bg="white",
)
window.geometry("800x1000")
window.resizable(False,False)
window.title("Tkinter GUI")

# variable dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_klik():
    pesan = f"hai {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, apa kabar?"
    showinfo(title="hai helo", message=pesan)

# frame input
frame_input = ttk.Frame(window)

# penempatan -> grid, pack, place
frame_input.pack(padx=40, pady=15, fill="x", expand=True)

# komponen-komponen
# 1. label nama depan
nama_depan_label = ttk.Label(frame_input, text="Nama Depan")
nama_depan_label.pack(padx=40, pady=15, fill="x", expand=True)

# 2. entry nama depan
nama_depan_entry = ttk.Entry(frame_input, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=40, pady=15, fill="x", expand=True)

# 3. lable nama belakang
nama_belakang_label = ttk.Label(frame_input, text="Nama Belakang")
nama_belakang_label.pack(padx=40, pady=15, fill="x", expand=True)

# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(frame_input, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=40, pady=15, fill="x", expand=True)

# tombol
tombol = ttk.Button(frame_input, text="klik", command=tombol_klik)
tombol.configure()
tombol.pack(padx=40, pady=15, fill="x", expand=True)

# mainloop window
window.mainloop()

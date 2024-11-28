# JUDUL STUDI KASUS : FORMAT APK PREMIUM

import tkinter as tk
from tkinter import ttk, messagebox
import re

class FromApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Format Apk PREMIUM")
        self.root.geometry("600x600")

        self.orders = []  # List untuk menyimpan daftar pesanan
        self.create_widget()

    def create_widget(self):
        # Title label
        title_label = tk.Label(self.root, text="Format APK PREMIUM", font=("Times New Roman", 15, 'bold'))
        title_label.pack(pady=5)

        # Nama Pemesan
        nama_label = tk.Label(self.root, text="Nama Pemesan:")
        nama_label.pack()
        self.nama_entry = tk.Entry(self.root, width=25)
        self.nama_entry.pack(pady=5)

        # Jenis Apk
        jenis_apk_label = tk.Label(self.root, text="Jenis Aplikasi:")
        jenis_apk_label.pack()
        self.jenis_var = tk.StringVar(value="")
        self.jenis_apk = ttk.Combobox(self.root, textvariable=self.jenis_var, state="readonly", width=25)
        self.jenis_apk['values'] = ["Netflix", "Canva"]
        self.jenis_apk.pack(pady=5)
        self.jenis_apk.bind("<<ComboboxSelected>>", self.update_from)

        # Keterangan (Netflix)
        ket_label = tk.Label(self.root, text="Keterangan (Netflix):")
        ket_label.pack()
        self.ket_var = tk.StringVar(value="")
        self.ket_apk = ttk.Combobox(self.root, textvariable=self.ket_var, state="readonly", width=25)
        self.ket_apk['values'] = ["Shar", "Priv"]
        self.ket_apk.pack(pady=5)

        # Email (Canva)
        email_label = tk.Label(self.root, text="Email (Canva):")
        email_label.pack()
        self.email_entry = tk.Entry(self.root, width=25)
        self.email_entry.pack(pady=5)

        # Durasi
        durasi_label = tk.Label(self.root, text="Durasi :")
        durasi_label.pack()
        self.durasi_var = tk.StringVar(value="")
        self.durasi_apk = ttk.Combobox(self.root, textvariable=self.durasi_var, state="readonly", width=25)
        self.durasi_apk['values'] = ["1 Tahun", "1 Bulan", "1 Minggu", "1 Hari"]
        self.durasi_apk.pack(pady=5)

        # Payment
        payment_label = tk.Label(self.root, text="Payment :")
        payment_label.pack()
        self.payment_var = tk.StringVar(value="")
        self.payment_apk = ttk.Combobox(self.root, textvariable=self.payment_var, state="readonly", width=25)
        self.payment_apk['values'] = ["BRI", "DANA"]
        self.payment_apk.pack(pady=5)

        # Harga
        self.price_label = tk.Label(self.root, text="Harga: Rp. 0", font=("Times New Roman", 12, 'bold'))
        self.price_label.pack(pady=5)

        # Tombol kirim format
        self.kirim_button = tk.Button(self.root, text="Kirim format", command=self.add_order)
        self.kirim_button.pack(pady=5)

        # Tombol hapus pesanan
        self.hapus_button = tk.Button(self.root, text="Hapus Pesanan", command=self.delete_order)
        self.hapus_button.pack(pady=5)

        # Daftar Pesanan
        daftar_pesanan_label = tk.Label(self.root, text="Daftar Pesanan:", font=("Times New Roman", 12, 'bold'))
        daftar_pesanan_label.pack()
        self.order_table = ttk.Treeview(self.root, columns=("Nama", "Jenis", "Keterangan/Email", "Durasi", "Harga", "Payment"), show="headings", selectmode="extended")
        self.order_table.heading("Nama", text="Nama")
        self.order_table.heading("Jenis", text="Jenis")
        self.order_table.heading("Keterangan/Email", text="Keterangan/Email")
        self.order_table.heading("Durasi", text="Durasi")
        self.order_table.heading("Harga", text="Harga")
        self.order_table.heading("Payment", text="Payment")

        self.order_table.column("Nama", width=100, anchor="center")
        self.order_table.column("Jenis", width=100, anchor="center")
        self.order_table.column("Keterangan/Email", width=150, anchor="center")
        self.order_table.column("Durasi", width=100, anchor="center")
        self.order_table.column("Harga", width=100, anchor="center")
        self.order_table.column("Payment", width=100, anchor="center")
        self.order_table.pack(pady=5)

        # Trace variables
        self.jenis_var.trace_add("write", self.update_price)
        self.ket_var.trace_add("write", self.update_price)
        self.durasi_var.trace_add("write", self.update_price)

    def update_from(self, event=None):
        jenis = self.jenis_var.get()
        if jenis == "Netflix":
            self.ket_apk.config(state="normal")
            self.email_entry.config(state="disabled")
        elif jenis == "Canva":
            self.email_entry.config(state="normal")
            self.ket_apk.config(state="disabled")

    def calculate_price(self):
        jenis = self.jenis_var.get()
        ket = self.ket_var.get()
        durasi = self.durasi_var.get()

        if jenis == "Netflix":
            if durasi == "1 Bulan":
                return "Rp. 19.000" if ket == "Shar" else "Rp. 27.000"
            if durasi == "1 Minggu":
                return "Rp. 14.500" if ket == "Shar" else "Rp. 15.500"
            if durasi == "1 Hari":
                return "Rp. 7.000" if ket == "Shar" else "Rp. 10.000"
            if durasi == "1 Tahun":
                return "Durasi tidak tersedia."

        elif jenis == "Canva":
            if durasi == "1 Tahun":
                return "Rp. 15.000"
            if durasi == "1 Bulan":
                return "Rp. 10.000"
            if durasi == "1 Minggu":
                return "Rp. 7.000"
            if durasi == "1 Hari":
                return "Rp. 5.000"

    def update_price(self, *args):
        price = self.calculate_price()
        self.price_label.config(text=f"Harga: {price}")

    def validate_email(self, email):
        return re.match(r"^[a-zA-Z0-9_.+-]+@gmail\.com$", email)

    def add_order(self):
        nama = self.nama_entry.get()
        jenis = self.jenis_var.get()
        ket = self.ket_var.get()
        email = self.email_entry.get()
        durasi = self.durasi_var.get()
        payment = self.payment_var.get()

        if not nama or not jenis or not durasi or not payment or (jenis == "Netflix" and not ket) or (jenis == "Canva" and not email):
            messagebox.showerror("Kesalahan", "Silakan isi semua form!")
            return

        if jenis == "Canva" and not self.validate_email(email):
            messagebox.showerror("Kesalahan", "Email Canva harus menggunakan @gmail.com!")
            return

        price = self.calculate_price()
        if "tidak tersedia" in price:
            messagebox.showerror("Kesalahan", "Durasi tidak tersedia untuk jenis aplikasi ini!")
            return

        order = (nama, jenis, ket if jenis == "Netflix" else email, durasi, price, payment)
        self.orders.append(order)
        self.order_table.insert("", "end", values=order)
        messagebox.showinfo("Sukses", "Pesanan berhasil ditambahkan!")

    def delete_order(self):
        selected_items = self.order_table.selection()
        if not selected_items:
            messagebox.showwarning("Peringatan", "Pilih pesanan yang ingin dihapus!")
            return
        for item in selected_items:
            self.order_table.delete(item)
        messagebox.showinfo("Sukses", "Pesanan berhasil dihapus!")

if __name__ == "__main__":
    root = tk.Tk()
    app = FromApp(root)
    root.mainloop()

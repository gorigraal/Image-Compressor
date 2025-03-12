import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def compress_image():
    input_path = entry_path.get()
    quality = int(scale_quality.get())
    
    if not os.path.exists(input_path):
        messagebox.showerror("Eroare", "Selectează o imagine validă!")
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if not output_path:
        return
    
    try:
        image = Image.open(input_path)
        image.save(output_path, "JPEG", quality=quality, optimize=True)
        messagebox.showinfo("Succes", f"Imaginea a fost comprimată și salvată la: {output_path}")
    except Exception as e:
        messagebox.showerror("Eroare", f"A apărut o problemă: {e}")

# Creare interfață
root = tk.Tk()
root.title("Comprimare Imagini")
root.geometry("400x250")

label = tk.Label(root, text="Selectează o imagine:")
label.pack()

entry_path = tk.Entry(root, width=50)
entry_path.pack()

btn_browse = tk.Button(root, text="Alege fișier", command=select_image)
btn_browse.pack()

label_quality = tk.Label(root, text="Calitate compresie (1-100):")
label_quality.pack()

scale_quality = tk.Scale(root, from_=10, to=100, orient="horizontal")
scale_quality.set(60)
scale_quality.pack()

btn_compress = tk.Button(root, text="Comprimă și salvează", command=compress_image)
btn_compress.pack()

root.mainloop()
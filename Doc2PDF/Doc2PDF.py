import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import subprocess
import os

# 🔧 Chemin vers LibreOffice (vérifie ce chemin si nécessaire)
CHEMIN_SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"

def convertir_avec_libreoffice(chemin_docx):
    dossier = os.path.dirname(chemin_docx)
    subprocess.run([
        CHEMIN_SOFFICE,
        "--headless",
        "--convert-to", "pdf",
        "--outdir", dossier,
        chemin_docx
    ], check=True)
    return os.path.splitext(chemin_docx)[0] + ".pdf"

def choisir_fichier():
    fichier = filedialog.askopenfilename(filetypes=[("Fichier Word", "*.docx")])
    if fichier:
        champ_fichier.delete(0, tk.END)
        champ_fichier.insert(0, fichier)

def lancer_conversion():
    fichier = champ_fichier.get()
    if not os.path.exists(fichier):
        messagebox.showerror("Erreur", "Fichier non trouvé.")
        return
    try:
        pdf = convertir_avec_libreoffice(fichier)
        messagebox.showinfo("Succès", f"PDF généré :\n{pdf}")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# === Interface ===
fenetre = tk.Tk()
fenetre.title("Convertisseur Word vers PDF")
fenetre.geometry("550x200")
fenetre.resizable(False, False)

style = ttk.Style()
if "vista" in style.theme_names():
    style.theme_use("vista")
else:
    style.theme_use("default")

# === Widgets ===
tk.Label(fenetre, text="Sélectionner un fichier Word :", font=("Segoe UI", 11)).pack(pady=(15, 5))

champ_fichier = ttk.Entry(fenetre, width=68)
champ_fichier.pack(ipady=3)

ttk.Button(fenetre, text="Parcourir", command=choisir_fichier).pack(pady=8)

ttk.Button(fenetre, text="Générer le PDF", command=lancer_conversion).pack(pady=5)

fenetre.mainloop()

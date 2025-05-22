# Doc2PDF

Bienvenue dans **Doc2PDF** ! Une application Python/Tkinter avec interface Windows classique, conçue pour convertir vos fichiers `.docx` en `.pdf` tout en conservant la mise en page originale.  
Elle repose sur LibreOffice pour une conversion fiable, sans dépendances payantes.

---

## 🚀 Fonctionnalités

- Conversion directe `.docx` → `.pdf`
- Interface graphique Windows simple et épurée
- Aucune modification du contenu ou du style original
- Fichier PDF généré dans le même dossier que le `.docx`
- Détection automatique du fichier sélectionné
- Messages d’erreur et de succès clairs

---

## 🖥️ Interface

- Thème **Vista** via `ttk.Style` pour un style Windows natif
- Champ d'entrée pour le chemin du fichier
- Boutons standards : **Parcourir** et **Générer le PDF**
- Mise en page compacte et fonctionnelle (550×200)

---

## 🛠️ Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/H4CK3R854/Doc2PDF.git
   cd Doc2PDF

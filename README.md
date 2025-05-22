# 📄 Doc2PDF

**Doc2PDF** est une application graphique simple et rapide pour convertir des fichiers **Word (.docx)** en **PDF** tout en conservant la mise en page d’origine.

Développée avec Python et LibreOffice, elle fonctionne **sans Microsoft Word**, **sans Adobe**, et offre une expérience fidèle, minimaliste et gratuite.

---

## 🚀 Fonctionnalités

- Interface graphique simple (Tkinter)
- Style Windows natif (boutons `vista`)
- Conversion en **1 clic**
- Conservation de :
  - Mise en page
  - Images
  - Tableaux
  - Styles de texte
- Génération automatique du fichier `.pdf` dans le même dossier que le `.docx`

---

## 🖼️ Aperçu

<img src="https://user-images.githubusercontent.com/your-image.png" alt="aperçu de l'application" width="450" />

---

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/H4CK3R854/Doc2PDF.git
cd Doc2PDF
2. Installer les dépendances Python
bash
Copier
Modifier
pip install -r requirements.txt
📌 Si tu n’as pas encore créé requirements.txt, voici ce qu’il doit contenir :

Copier
Modifier
txt
Copier
Modifier
# requirements.txt
(pas nécessaire, car le script utilise uniquement Tkinter – déjà inclus avec Python)

3. Installer LibreOffice (obligatoire)
🔗 Télécharger LibreOffice

Le chemin par défaut utilisé est :

bash
Copier
Modifier
C:\Program Files\LibreOffice\program\soffice.exe
Si tu l’as installé ailleurs, modifie cette ligne dans doc2pdf.py :

python
Copier
Modifier
CHEMIN_SOFFICE = r"C:\Program Files\LibreOffice\program\soffice.exe"
▶️ Utilisation
Lance l'application avec Python :

bash
Copier
Modifier
python doc2pdf.py
Clique sur Parcourir pour sélectionner un fichier .docx

Clique sur Générer le PDF

Le PDF est créé dans le même dossier que le fichier Word original.

✅ Prérequis
Windows (10/11)

Python 3.8+

LibreOffice installé

🛠️ Personnalisation
Tu peux facilement :

Modifier l'apparence de l'interface

Ajouter un logo

Intégrer la conversion par lot de fichiers

Choisir un dossier de sortie personnalisé

📖 Licence
Ce projet est distribué sous licence MIT — utilisation libre.

👤 Auteur
Développé par H4CK3R854
🔗 Dépôt : https://github.com/H4CK3R854/Doc2PDF

yaml
Copier
Modifier

---

Tu peux :
- Ajouter une capture d'écran dans le dossier du repo et remplacer `your-image.png`
- Créer le fichier `README.md` et y coller ce contenu
- Ajouter un `requirements.txt` vide (ou rien si `tkinter` suffit)

Souhaite-tu que je te fasse aussi un **setup .exe** ou un **script d'installation automatique** ?








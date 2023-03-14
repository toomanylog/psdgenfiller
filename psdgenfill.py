from PIL import Image
from io import BytesIO
import requests
from faker import Faker

# Chemin du fichier PSD
PSD_PATH = "chemin/vers/votre/fichier.psd"

# URL de l'API Unsplash pour télécharger des images aléatoires de selfie
UNSPLASH_API_URL = "https://source.unsplash.com/400x400/?selfie"

# Initialise la bibliothèque Faker
fake = Faker()

# Génère des informations aléatoires
nom = fake.last_name()
prenom = fake.first_name()
id_membre = fake.unique.random_number(digits=8)

# Télécharge une image de selfie aléatoire depuis Unsplash
response = requests.get(UNSPLASH_API_URL)
selfie = Image.open(BytesIO(response.content))

# Charge le fichier PSD
image = Image.open(PSD_PATH)

# Redimensionne l'image de selfie pour qu'elle rentre dans le cadre prévu dans le PSD
selfie.thumbnail((200, 200))

# Dessine l'image de selfie sur le PSD
image.paste(selfie, (500, 100))

# Initialise le dessin
draw = ImageDraw.Draw(image)

# Charge la police de caractères
font = ImageFont.truetype("Chemin/vers/votre/police.ttf", 30)

# Remplace chaque champ de texte dans le PSD avec les informations générées
draw.text((100, 100), nom, font=font)
draw.text((100, 200), prenom, font=font)
draw.text((100, 300), str(id_membre), font=font)

# Enregistre l'image générée
image.save("chemin/vers/votre/fichier_genere.png", "PNG")

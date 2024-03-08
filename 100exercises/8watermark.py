import os
import glob
from PIL import Image

logo_path = 'gojo.png'
carpeta = r"C:\Users\Acer\Documents\CursoPython\projectcv\imagenes"
patron = "*JPG"
imagenes = glob.glob(os.path.join(carpeta, patron))

logo = Image.open(logo_path)
logo = logo.resize((180,180))

for imagenes_path in imagenes:
    imagen = Image.open(imagenes_path)
    position = (int(imagen.width/2)-90, int(imagen.height/2)-90)
    imagen.paste(logo,position, logo)
    imagen.save(imagenes_path)

from googletrans import Translator
import pyttsx3

traductor = Translator()

try:
    with open('Traductor/libro.txt', mode='r') as miArchivo:
        texto = miArchivo.read()
        TextoTraducido = traductor.translate(text = texto)
        print(TextoTraducido)
except FileNotFoundError as error:
    print('Error: ', error)
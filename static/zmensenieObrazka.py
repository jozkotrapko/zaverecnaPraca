from PIL import Image

originalObrazok = 'ruka.png'
zmensitObrazok = 'ruka.png'


with Image.open(originalObrazok) as img:
    novaVelkost = (300, 300)
    zmensit_img = img.resize(novaVelkost)

    zmensit_img.save(zmensitObrazok)

print("Obrázok bol zmenšený a uložený do", zmensitObrazok)
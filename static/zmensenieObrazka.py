from PIL import Image

originalObrazok = 'pythonLogo.png'
zmensitObrazok = 'pythonLogo.png'


with Image.open(originalObrazok) as img:
    novaVelkost = (280, 280)
    zmensit_img = img.resize(novaVelkost)

    zmensit_img.save(zmensitObrazok)

print("Obrázok bol zmenšený a uložený do", zmensitObrazok)
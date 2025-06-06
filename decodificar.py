from tkinter import filedialog, Tk
from PIL import Image

def revelar_mensagem():
    # Interface para escolher imagem
    Tk().withdraw()
    caminho_imagem = filedialog.askopenfilename(title="Escolha a imagem codificada")
    if not caminho_imagem:
        print("Nenhuma imagem escolhida.")
        return

    img = Image.open(caminho_imagem)
    pixels = img.load()
    largura, altura = img.size

    binario = ""
    for y in range(altura):
        for x in range(largura):
            r, g, b = pixels[x, y]
            binario += str(r & 1)

    # Agrupar em bytes (8 bits)
    bytes_mensagem = [binario[i:i+8] for i in range(0, len(binario), 8)]
    mensagem = ""
    for byte in bytes_mensagem:
        char = chr(int(byte, 2))
        if char == chr(0):  # fim da mensagem
            break
        mensagem += char

    print(f"\n⚜️{mensagem}⚜️\n")

revelar_mensagem()


# https://linktr.ee/juavi
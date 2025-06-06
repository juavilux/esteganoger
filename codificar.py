from tkinter import filedialog, Tk, simpledialog
from PIL import Image

def esconder_mensagem():
    # Interface para escolher imagem
    Tk().withdraw()
    caminho_imagem = filedialog.askopenfilename(title="Escolha a imagem")
    if not caminho_imagem:
        print("Você ainda não escolheu uma imagem.")
        return

    # Solicita mensagem ao usuário
    mensagem = simpledialog.askstring("ESTEGANOGER", "Escreva sua esteganografia:")
    if not mensagem:
        print("Forneça uma escrita para continuarmos.")
        return

    mensagem += chr(0)  # Delimitador de fim
    binario = ''.join(format(ord(c), '08b') for c in mensagem)

    img = Image.open(caminho_imagem)
    # Converte a imagem para modo RGB, se necessário
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()
    largura, altura = img.size

    # Verifica se a imagem tem espaço suficiente para a mensagem
    if len(binario) > largura * altura:
        print("Erro: A mensagem é extensa.")
        return

    i = 0
    for y in range(altura):
        for x in range(largura):
            if i >= len(binario):
                break
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binario[i])  # Altera o bit menos significativo do canal vermelho
            pixels[x, y] = (r, g, b)
            i += 1

    caminho_saida = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Salvar imagem codificada"
    )
    if caminho_saida:
        img.save(caminho_saida)
        print(f"Mensagem criptografada com sucesso em: {caminho_saida}")

esconder_mensagem()
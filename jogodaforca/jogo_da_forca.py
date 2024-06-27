import tkinter as tk
import random
from tkinter import messagebox

palavras = {
    "comidas": ["pizza", "hamburguer", "sushi", "lasanha", "churrasco", "banana", "laranja", "uva", "abacaxi", "morango",
      "melancia", "pera", "manga", "kiwi", "amora", "framboesa",
      "caju"],
    "objetos": [ "cadeira", "mesa", "livro", "caneta", "telefone", "notebook",
      "escrivaninha", "porta", "relogio", "copo", "luminaria", "espelho",
      "prato", "travesseiro", "tesoura"],
    "animais": ["cachorro", "gato", "elefante", "leao", "tigre", "zebra", "girafa",
      "macaco", "cavalo", "coelho", "panda", "koala", "canguru",
      "raposa"]
}

# Função para escolher uma palavra aleatória
def escolher_palavra():
    categorias = list(palavras.keys())
    categoria = random.choice(categorias)
    palavra = random.choice(palavras[categoria])
    return palavra, categoria


def desenhar_forca(erros):
    canvas.delete("forca")
    if erros == 1:
        canvas.create_image(500, 500, image=imagens["forca"], tags="forca")
    if erros == 2:
        canvas.create_image(500, 500, image=imagens["cabeca"], tags="forca")
    if erros == 3:
        canvas.create_image(500, 500, image=imagens["rosto"], tags="forca")
    if erros == 4:
        canvas.create_image(500, 500, image=imagens["tronco"], tags="forca")
    if erros == 5:
        canvas.create_image(500, 500, image=imagens["braco1"], tags="forca")
    if erros == 6:
        canvas.create_image(500, 500, image=imagens["braco2"], tags="forca")
    if erros == 7:
        canvas.create_image(500, 500, image=imagens["perna1"], tags="forca")
    if erros == 8:
        canvas.create_image(500, 500, image=imagens["perna2"], tags="forca")
    if erros == 9:
        canvas.create_image(500, 500, image=imagens["corda"], tags="forca")
    if erros == 10:
        canvas.create_image(500, 500, image=imagens["morte"], tags="forca")

def iniciar_jogo():
    global palavra_secreta, categoria, letras_usadas, erros
    palavra_secreta, categoria = escolher_palavra()
    letras_usadas = []
    erros = 0
    desenhar_forca(erros)
    atualizar_interface()

    


def atualizar_interface():
    palavra_display = ""
    for letra in palavra_secreta:
        if letra in letras_usadas:
            palavra_display += letra + " "
        else:
            palavra_display += "_ "
    label_palavra.config(text=palavra_display)
    label_categoria.config(text="Categoria: " + categoria)
    label_letras.config(text="Letras usadas: " + ", ".join(letras_usadas))
    label_erros.config(text="Erros: " + str(erros) + "/10")


def verificar_letra(event):
    global letras_usadas, erros
    letra = event.char.lower()
    if letra in letras_usadas:
        return
    letras_usadas.append(letra)
    if letra not in palavra_secreta:
        erros += 1
        desenhar_forca(erros)
    atualizar_interface()
    if erros == 10:
        messagebox.showinfo("Você perdeu!", f"A palavra era: {palavra_secreta}")
        reset_game()
    elif all(letra in letras_usadas for letra in palavra_secreta):
        messagebox.showinfo("Você ganhou!", f"A palavra era: {palavra_secreta}")
        reset_game()

def reset_game():
    global letras_usadas, label_resultado, label_erros, erros
    letras_usadas = []
    label_resultado["text"] = ""
    erros = 0

janela = tk.Tk()
janela.title("Jogo da Forca")
janela.configure(bg="#add8e6")

imagens = {
    "forca": tk.PhotoImage(file="forca.png").subsample(1, 1),
    "cabeca": tk.PhotoImage(file="head.png").subsample(1, 1),
    "rosto": tk.PhotoImage(file="rosto.png").subsample(1, 1),
    "tronco": tk.PhotoImage(file="body.png").subsample(1, 1),
    "braco1": tk.PhotoImage(file="arm1.png").subsample(1, 1),
    "braco2": tk.PhotoImage(file="arm2.png").subsample(1, 1),
    "perna1": tk.PhotoImage(file="leg1.png").subsample(1, 1),
    "perna2": tk.PhotoImage(file="leg2.png").subsample(1, 1),
    "corda": tk.PhotoImage(file="morte.png").subsample(1, 1),
    "morte": tk.PhotoImage(file="morte2.png").subsample(1, 1)
}


canvas = tk.Canvas(janela, width=1280, height=720, bg="#add8e6")
canvas.pack()


label_titulo = tk.Label(janela, text="Jogo da Forca", font=("Arial", 36), fg="white", bg="#add8e6")
label_titulo.place(x=75, y=20)

label_palavra = tk.Label(janela, font=("Arial", 28), fg="white", bg="#add8e6")
label_palavra.place(x=100, y=100)

label_categoria = tk.Label(janela, font=("Arial", 18), fg="white", bg="#add8e6")
label_categoria.place(x=100, y=150)

label_letras = tk.Label(janela, font=("Arial", 16), fg="white", bg="#add8e6")
label_letras.place(x=100, y=200)

label_erros = tk.Label(janela, font=("Arial", 16), fg="white", bg="#add8e6")
label_erros.place(x=100, y=250)

label_resultado = tk.Label(janela,text= "",  font=("Arial", 28), fg="white", bg="#add8e6")
label_resultado.place(x=100, y=300)


botao_iniciar = tk.Button(janela, text="Iniciar Jogo", command=iniciar_jogo, bg="#4169e1", fg="white", font=("Arial", 16))
botao_iniciar.place(x=150, y=375)

janela.bind("<Key>", verificar_letra)




janela.mainloop()
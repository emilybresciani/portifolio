import random
import tkinter as tk

titulos_nossa_senhora = [
    "Nossa Senhora Aparecida",
    "Nossa Senhora de Fátima",
    "Nossa Senhora das Graças",
    "Nossa Senhora de Lourdes",
    "Nossa Senhora do Rosário",
    "Nossa Senhora do Carmo",
    "Nossa Senhora da Conceição",
    "Nossa Senhora Auxiliadora",
    "Nossa Senhora de Guadalupe",
    "Nossa Senhora Rainha da Paz",
    "Nossa Senhora da Penha",
    "Nossa Senhora da Medalha Milagrosa",
    "Nossa Senhora das Dores",
    "Nossa Senhora da Luz",
    "Nossa Senhora da Boa Viagem",
    "Nossa Senhora da Esperança",
    "Nossa Senhora da Saúde",
    "Nossa Senhora do Perpétuo Socorro",
    "Nossa Senhora Mãe de Deus",
    "Nossa Senhora Estrela do Mar",
    "Nossa Senhora dos Navegantes",
    "Nossa Senhora da Piedade",
    "Nossa Senhora da Imaculada Conceição",
    "Nossa Senhora da Assunção",
    "Nossa Senhora da Anunciação"
]

def sorteio():
    titulo = random.choice(titulos_nossa_senhora)
    label_resultado.config(text=f"{titulo}") 

jan = tk.Tk()
jan.title("Sorteio de Títulos de Nossa Senhora")
jan.geometry("400x250")
jan.configure(bg="#0f77ff")

label_titulo = tk.Label(jan, text="Clique no botão para sortear um título de Nossa Senhora", font=("Arial", 12), bg="#0f77ff", fg="white")
label_titulo.pack(pady=20)

botao_sorteio = tk.Button(jan, text="Sortear", font=("Georgia", 12), command=sorteio, bg="#000296", fg="white", padx=20, pady=10, borderwidth=0, relief="raised")
botao_sorteio.pack(pady=10)

label_sorteio = tk.Label(jan, text="Título sorteado:", font=("Arial", 12), bg="#0f77ff", fg="white")
label_sorteio.pack(pady=10)

label_resultado = tk.Label(jan, text="", font=("Arial", 12), bg="#0f77ff", fg="white")
label_resultado.pack(pady=20)

jan.mainloop()


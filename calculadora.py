import tkinter as tk

conta=""

def botao(num):
    global conta

    conta = conta +str(num)

    visor.set(conta)

def calcular():
    try:
        global conta
        resultado = eval (conta)
        visor.set(str(resultado))
        conta = str(resultado)

    except:
        visor.set("Erro")
        conta = ""

def limpar ():
    global conta
    conta = ""
    visor.set("")

jan = tk.Tk()
jan.title("Calculadora da Bresci")
jan.geometry("300x400")
jan.configure(bg="#BD4AFF")

visor = tk.StringVar()

display = tk.Entry(jan, textvariable=visor, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=0, justify='right')
display.grid(columnspan=4, ipady=15, padx=10, pady=10)

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (texto, linha, coluna) in botoes:

    if texto == 'C':
        faz = limpar

    elif texto == '=':
        faz = calcular

    else:
        faz = lambda x = texto: botao(x)

    btn = tk.Button(jan, text=texto, fg='#000000', font=('Arial', 14), command=faz, height=2, width=5)
    btn.grid(row=linha, column=coluna, padx=5, pady=5)

jan.mainloop()
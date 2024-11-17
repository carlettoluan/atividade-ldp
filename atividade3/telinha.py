import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        altura = float(entry_altura.get())
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)
        resultado_texto.set(f"IMC: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")

# Função para reiniciar os campos de entrada
def reiniciar_campos():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_texto.set("")

# Função para sair da aplicação
def sair_app():
    root.destroy()

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Criar e posicionar os rótulos e campos de entrada
tk.Label(root, text="Nome do Paciente:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço Completo:").grid(row=1, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Altura (m):").grid(row=2, column=0, padx=10, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Peso (kg):").grid(row=3, column=0, padx=10, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=3, column=1, padx=10, pady=5)

# Criar e posicionar o rótulo de resultado
resultado_texto = tk.StringVar()
tk.Label(root, textvariable=resultado_texto).grid(row=4, columnspan=2, padx=10, pady=5)

# Criar e posicionar os botões
tk.Button(root, text="Calcular", command=calcular_imc).grid(row=5, column=0, padx=10, pady=5)
tk.Button(root, text="Reiniciar", command=reiniciar_campos).grid(row=5, column=1, padx=10, pady=5)
tk.Button(root, text="Sair", command=sair_app).grid(row=6, columnspan=2, padx=10, pady=5)

# Executar a aplicação
root.mainloop()
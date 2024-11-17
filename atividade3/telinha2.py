import tkinter as tk
from tkinter import messagebox

def calculateBMI():
    try:
        weight = float(entryWeight.get())
        height = float(entryHeight.get())
        bmi = weight / (height ** 2)
        
        if bmi < 18.5:
            result = f"IMC: {bmi:.2f} (Abaixo do peso)"
        elif 18.5 <= bmi < 24.9:
            result = f"IMC: {bmi:.2f} (Peso normal)"
        elif 25 <= bmi < 29.9:
            result = f"IMC: {bmi:.2f} (Sobrepeso)"
        else:
            result = f"IMC: {bmi:.2f} (Obesidade)"
        
        lblResult.config(text=result)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

def resetFields():
    entryName.delete(0, tk.END)
    entryAddress.delete(0, tk.END)
    entryHeight.delete(0, tk.END)
    entryWeight.delete(0, tk.END)
    lblResult.config(text="")

def exitApp():
    window.quit()

# Configuração da janela principal
window = tk.Tk()
window.title("Cálculo de IMC")
window.geometry("400x400")

# Labels e entradas
tk.Label(window, text="Nome do Paciente:").pack(pady=5)
entryName = tk.Entry(window, width=30)
entryName.pack()

tk.Label(window, text="Endereço Completo:").pack(pady=5)
entryAddress = tk.Entry(window, width=30)
entryAddress.pack()

tk.Label(window, text="Altura (em metros):").pack(pady=5)
entryHeight = tk.Entry(window, width=30)
entryHeight.pack()

tk.Label(window, text="Peso (em kg):").pack(pady=5)
entryWeight = tk.Entry(window, width=30)
entryWeight.pack()

# Botões
tk.Button(window, text="Calcular", command=calculateBMI, width=15).pack(pady=10)
tk.Button(window, text="Reiniciar", command=resetFields, width=15).pack(pady=5)
tk.Button(window, text="Sair", command=exitApp, width=15).pack(pady=5)

# Resultado
lblResult = tk.Label(window, text="", font=("Arial", 12), fg="blue")
lblResult.pack(pady=20)

# Loop principal da interface
window.mainloop()

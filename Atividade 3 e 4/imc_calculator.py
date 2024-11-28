import tkinter as tk
from tkinter import ttk
import sqlite3

def save_to_db(name, address, weight, height, bmi):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, address TEXT, weight REAL, height REAL, bmi REAL)''')
    cursor.execute('''INSERT INTO users (name, address, weight, height, bmi) 
                      VALUES (?, ?, ?, ?, ?)''', (name, address, weight, height, bmi))
    conn.commit()
    conn.close()

def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def submit_form():
    try:
        name = entry_name.get()
        address = entry_address.get()
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Peso e altura devem ser positivos.")
        bmi = calculate_bmi(weight, height)
        save_to_db(name, address, weight, height, bmi)
        result_var.set(f"IMC: {bmi:.2f}")
    except ValueError as e:
        result_var.set(f"Erro: {e}")
    except Exception as e:
        result_var.set("Erro: Dados inválidos.")

root = tk.Tk()
root.title("Calculadora de IMC (Índice de Massa Corporal)")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_name = ttk.Label(frame, text="Nome:")
label_name.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_name = ttk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

label_address = ttk.Label(frame, text="Endereço:")
label_address.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_address = ttk.Entry(frame, width=30)
entry_address.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=tk.W)

label_weight = ttk.Label(frame, text="Peso (kg):")
label_weight.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
entry_weight = ttk.Entry(frame, width=30)
entry_weight.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

label_height = ttk.Label(frame, text="Altura (cm):")
label_height.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
entry_height = ttk.Entry(frame, width=30)
entry_height.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

result_var = tk.StringVar()
label_result = ttk.Label(frame, textvariable=result_var)
label_result.grid(row=2, column=2, rowspan=2, padx=5, pady=5, sticky=tk.W)

submit_button = ttk.Button(frame, text="Enviar", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

# mainframe
root.mainloop()

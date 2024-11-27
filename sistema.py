import tkinter as tk
from tkinter import ttk
import time

# Función para mostrar la barra de carga
def mostrar_barra_carga():
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.03)
    ventana_principal()

# Función para calcular el total
def calcular_total():
    total = 0
    for item in lista_pedidos:
        total += item['precio']
    total_label.config(text=f"Total: ${total:.2f}")

# Función para agregar un pedido
def agregar_pedido():
    tipo = tipo_var.get()
    sabor = sabor_var.get()
    precio = float(precio_var.get())
    lista_pedidos.append({'tipo': tipo, 'sabor': sabor, 'precio': precio})
    lista_pedidos_texto.insert(tk.END, f"{tipo} de {sabor} - ${precio:.2f}\n")
    calcular_total()

# Función para mostrar la ventana principal
def ventana_principal():
    barra_carga_frame.pack_forget()
    ventana_principal_frame.pack()

# Función para abrir la calculadora
def abrir_calculadora():
    calculadora = tk.Toplevel(root)
    calculadora.title("Calculadora")
    
    def click(boton):
        current = entrada.get()
        entrada.delete(0, tk.END)
        entrada.insert(0, current + str(boton))
    
    def clear():
        entrada.delete(0, tk.END)
    
    def igual():
        try:
            result = eval(entrada.get())
            entrada.delete(0, tk.END)
            entrada.insert(0, str(result))
        except:
            entrada.delete(0, tk.END)
            entrada.insert(0, "Error")
    
    entrada = tk.Entry(calculadora, width=16, font=('Arial', 18), borderwidth=2, relief="solid")
    entrada.grid(row=0, column=0, columnspan=4)
    
    botones = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]
    
    row_val = 1
    col_val = 0
    for boton in botones:
        action = lambda x=boton: click(x)
        if boton == "=":
            tk.Button(calculadora, text=boton, width=10, height=3, command=igual).grid(row=row_val, column=col_val, columnspan=2)
            col_val += 2
        else:
            tk.Button(calculadora, text=boton, width=5, height=3, command=action).grid(row=row_val, column=col_val)
            col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1
    
    tk.Button(calculadora, text="C", width=5, height=3, command=clear).grid(row=row_val, column=0)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Sistema de Empanadas")

# Frame para la barra de carga
barra_carga_frame = tk.Frame(root)
barra_carga_frame.pack(pady=20)
bienvenida_label = tk.Label(barra_carga_frame, text="Bienvenido/a al puesto de empanadas", font=("Helvetica", 16))
bienvenida_label.pack(pady=10)
progress = ttk.Progressbar(barra_carga_frame, orient=tk.HORIZONTAL, length=300, mode='determinate')
progress.pack(pady=10)

# Frame para la ventana principal
ventana_principal_frame = tk.Frame(root)

# Variables
tipo_var = tk.StringVar()
sabor_var = tk.StringVar()
precio_var = tk.StringVar()
lista_pedidos = []

# Widgets de la ventana principal
pedido_frame = tk.Frame(ventana_principal_frame)
pedido_frame.grid(row=0, column=0, padx=10, pady=5)

tk.Label(pedido_frame, text="Tipo de Empanada:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(pedido_frame, textvariable=tipo_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(pedido_frame, text="Sabor del Jugo:").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(pedido_frame, textvariable=sabor_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(pedido_frame, text="Precio:").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(pedido_frame, textvariable=precio_var).grid(row=2, column=1, padx=10, pady=5)

tk.Button(pedido_frame, text="Agregar Pedido", command=agregar_pedido).grid(row=3, column=0, columnspan=2, pady=10)

lista_pedidos_texto = tk.Text(pedido_frame, height=10, width=40)
lista_pedidos_texto.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

total_label = tk.Label(pedido_frame, text="Total: $0.00", font=("Helvetica", 14))
total_label.grid(row=5, column=0, columnspan=2, pady=10)

# Tabla de precios
menu_frame = tk.Frame(ventana_principal_frame)
menu_frame.grid(row=0, column=1, padx=10, pady=5)

tk.Label(menu_frame, text="Menú", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=3)
tk.Label(menu_frame, text="Producto").grid(row=1, column=0)
tk.Label(menu_frame, text="Tipo").grid(row=1, column=1)
tk.Label(menu_frame, text="Precio").grid(row=1, column=2)

productos = [
    {"producto": "Empanada", "tipo": "Carne", "precio": 1.50},
    {"producto": "Empanada", "tipo": "Pollo", "precio": 1.50},
    {"producto": "Empanada", "tipo": "Queso", "precio": 1.50},
    {"producto": "Jugo", "tipo": "Naranja", "precio": 1.00},
    {"producto": "Jugo", "tipo": "Manzana", "precio": 1.00},
    {"producto": "Jugo", "tipo": "Uva", "precio": 1.00},
]

for i, producto in enumerate(productos, start=2):
    tk.Label(menu_frame, text=producto["producto"]).grid(row=i, column=0)
    tk.Label(menu_frame, text=producto["tipo"]).grid(row=i, column=1)
    tk.Label(menu_frame, text=f"${producto['precio']:.2f}").grid(row=i, column=2)

# Botón para abrir la calculadora
tk.Button(ventana_principal_frame, text="Caja Registradora", command=abrir_calculadora).grid(row=1, column=0, columnspan=2, pady=10)

# Iniciar la barra de carga
root.after(100, mostrar_barra_carga)

root.mainloop()

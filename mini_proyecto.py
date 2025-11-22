import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Lista de tareas')
ventana.geometry('400x320')

### Reloj Función simple ###
def actualizar_hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text=tiempo_actual)
    ventana.after(1000, actualizar_hora)

reloj = tk.Label(ventana, font=('Arial', 12, 'bold'), fg='blue')
reloj.place(relx=1.0, y=10, anchor='ne')  # esquina superior derecha
actualizar_hora()

### Título ###
titulo = tk.Label(ventana, text='Ingrese una tarea', font=('Arial', 12, 'bold'))
titulo.pack(pady=(10, 5))

### Campo de entrada ###
ingreso_tarea = tk.Entry(ventana, width=40)
ingreso_tarea.pack(pady=5)

### Menú desplegable ###
categorias = ['Compras', 'Trabajo', 'Eventos', 'Deporte', 'Entretenimiento']
categoria_seleccionada = tk.StringVar(value=categorias[0])

menu_categoria = tk.OptionMenu(ventana, categoria_seleccionada, *categorias)
menu_categoria.pack(pady=5)


def agregar_tarea():
    tarea = ingreso_tarea.get()
    categoria = categoria_seleccionada.get()
    if tarea:
        texto_final = f"{tarea} - {categoria}"
        lista_tareas.insert(tk.END, texto_final)
        ingreso_tarea.delete(0, tk.END)


boton_agregar = tk.Button(ventana, text='Agregar tarea', command=agregar_tarea)
boton_agregar.pack(pady=5)


def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)


boton_eliminar = tk.Button(ventana, text='Eliminar tarea', command=eliminar_tarea)
boton_eliminar.pack(pady=5)

### Barra de desplazamiento ###
marco = tk.Frame(ventana)
marco.pack(pady=10, fill='both', expand=True)

### Lista de tareas con Scrollbar ###
scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side='right', fill='y')

lista_tareas = tk.Listbox(marco, width=50, yscrollcommand=scrollbar.set)
lista_tareas.pack(side='left', fill='both', expand=True)

scrollbar.config(command=lista_tareas.yview)

ventana.mainloop()
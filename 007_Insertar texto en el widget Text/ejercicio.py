import tkinter as tk
#ventana principal
ventana=tk.Tk()
ventana.title("interfas")
ventana.geometry("500x300")
contador=0
#widget text
texto=tk.Text(ventana, width=50, height=15)
texto.pack()

#funcion para incertar text
def insert_texto():
    global contador 
    contador +=1
    texto.insert(tk.END,f"¡linea {contador}!\n")



#boton para llamar a la funcion incert texto
boton_insertar=tk.Button(ventana,text="insertar texto",command=insert_texto)
boton_insertar.pack()

#bucle principal
ventana.mainloop()
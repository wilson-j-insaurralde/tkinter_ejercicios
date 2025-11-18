import tkinter as tk

# ventana principal 
ventana=tk.Tk()
ventana.title("interfas grafica")
ventana.geometry("500x300")

#widget text 
texto = tk.Text(ventana, width=50,height=15)
texto.pack()

#insaertamos algo de texto 

texto.insert("1.0","primeralinea.\n")
texto.insert("2.0","segundalinea.\n")
texto.insert("3.0","terceralinea.\n")

#funcion para eliminar texto en el widget text
def eliminar_texto():
    texto.delete("1.0", tk.END)

#boton para llamar ala funcion eliminacion de texto 
boton_eliminar = tk.Button(ventana,text="eliminar texto",command=eliminar_texto)
boton_eliminar.pack()

#bucle principal 
ventana.mainloop()
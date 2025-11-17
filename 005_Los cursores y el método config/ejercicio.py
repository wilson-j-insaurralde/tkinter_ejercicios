#importacion tkinter
import tkinter as tk 

# creacion y configuracion de la ventana
ventana= tk.Tk()
ventana.title("mi primer programa tkinter")
ventana.geometry("500x300+300+150")  #+x+y ubicaciones donde aparece


ventana.config(cursor="hand2") #cursosr de la ventana 

#entrada de texto 
entrada=tk.Entry(ventana)
entrada.pack()

entrada.config(cursor="hand2") #cursor del boton


#bucle ventana
ventana.mainloop()
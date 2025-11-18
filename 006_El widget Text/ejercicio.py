#importacion tkinter
import tkinter as tk 

# creacion y configuracion de la ventana
ventana= tk.Tk()
ventana.title("mi primer programa tkinter")
ventana.geometry("500x300+300+150")  
#widget tex
texto=tk.Text(ventana)
texto.config(width=25, height=10)

texto.pack()





#bucle ventana
ventana.mainloop()
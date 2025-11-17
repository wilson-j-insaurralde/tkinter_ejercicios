#importacion tkinter
import tkinter as tk 

# creacion y configuracion de la ventana
ventana= tk.Tk()
ventana.title("mi primer programa tkinter")
ventana.geometry("500x300+300+150")  

#entrada de texto 
entrada= tk.Entry(ventana,
                  background="beige",
                  foreground="blue"
                  )
entrada.pack()


#bucle ventana
ventana.mainloop()
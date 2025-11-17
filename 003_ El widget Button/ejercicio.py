#importacion tkinter
import tkinter as tk 

# creacion y configuracion de la ventana
ventana= tk.Tk()
ventana.title("mi primer programa tkinter")
ventana.geometry("500x300+300+150")  #+x+y ubicaciones donde aparece
ventanaSecundaria=tk.Toplevel()#crea una ventana secundaria
#boton
boton=tk.Button(ventana,# ventana donde se muestra
                text="tocame",
                font=("arial",15,"bold"),
                bg="green2",
                fg="gold",
                activebackground="white",#color al pulsar de fondo
                activeforeground="red", #color al pulsar de la letra 
                borderwidth=5 ,
                relief="flat", #relive del borde
                )

boton.pack()

#bucle ventana
ventana.mainloop()

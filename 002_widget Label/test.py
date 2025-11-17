#importacion tkinter
import tkinter as tk 

# creacion y configuracion de la ventana
ventana= tk.Tk()
ventana.title("mi primer programa tkinter")
ventana.geometry("500x300")  
#crear funte personalizada 
fuentePersonalizada=("Roboto", 36,"bold")#tipografia
#etiqueta 
etiqueta=tk.Label(text="¡hola mundo!" ,
                  bg="gold",#brackground o bg color de fondo
                  fg="red" ,#foreground o fg color letra
                  bd=10  , #borderwidth border o bd bordes 
                  cursor="hand2",#efecto del cursor sobre el boton 
                  state=tk.DISABLED     , #estado del boton 
                  disabledforeground="sky blue" ,#color estado deshabilitado
                  font=fuentePersonalizada,#la trae
                     )  

#muestra la etiqueta en la ventana 
etiqueta.pack()


#bucle ventana
ventana.mainloop()

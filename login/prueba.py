from tkinter import *
class documento():
    def __init__(self,boton):
        self.boton=boton
        self.boton.title('bienvenido')
        self.boton_documento=Button(boton,text='boton',command=self.comando)
        self.boton_documento.pack()
        self.linea1=StringVar
        self.linea=Entry(boton,textvar=self.linea1)
        self.linea.pack()
    def comando(self):
        from guardado import entrada
        entrada(self)


root=Tk()
ven=documento(root)
root.mainloop()



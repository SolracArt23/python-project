from tkinter import *
from tkinter import ttk
from gtts import gTTS
import os

class ventana:
    def __init__(self,lector):
        self.ventana=lector
        self.ventana.title('LECTOR V 2.0')
        self.ventana.geometry('300x450')
        self.ventana.config(bg= 'red')
    #variables
        self.guardar=StringVar
    #marco
        self.marco=Frame(lector,width=280,height=435)
        self.marco.pack()
        self.marco.propagate(0)
    #iconos e imagenes
        self.play=PhotoImage(file='imagenes/play.png')
        self.clip=PhotoImage(file='imagenes/clip.png')
        #self.basura=PhotoImage()

    #titulo
        self.titulo=Label(self.marco,text='lector',font=('Arial',16))
        self.titulo.pack()
    #barra de texto
        self.texto=Text(self.marco, state='normal',width=30,height=18)
        self.texto.pack()
        self.texto.insert(INSERT,'el boton de play es aquel que se encargara de reproduccir lo escrito y el del clip no  funciona :,(')
    #barra de crear titulo
        self.nombre=Label(self.marco,text='titulo de el archivo',font=('Arial',11))
        self.nombre.pack()
        self.nombre.place(x=15, y=325)
        #funcion
        self.titular=Entry(self.marco,textvar=self.guardar,width=25)
        self.titular.pack()
        self.titular.place(x=15, y=348)
    #barra de idioma
        self.nombre2 = Label(self.marco, text='selec. idioma ', font=('Arial', 11))
        self.nombre2.pack()
        self.nombre2.place(x=15, y=375)
        #funcio
        self.barra=ttk.Combobox(self.marco,width=22,state='readonly')
        self.barra.pack()
        self.barra['values']=['','es','en','fr']
        self.barra.place(x=15, y=398)
    #boton
        #boton de play
        self.boton=Button(self.marco,image=self.play,command=self.p)
        self.boton.pack()
        self.boton.place(x=180,y=370)
        # boton de clip
        self.botonClip=Button(self.marco,image=self.clip,command=self.enlace)
        self.botonClip.pack()
        self.botonClip.place(x=230,y=370)
    def p (self):
        self.gtexto=self.texto.get('1.0','end')
        self.guardado=self.titular.get()
        self.inport=ventana
        self.inport.programas(self)


    def enlace(self):
        self.Os=os
        self.Os.startfile('explorer.exe')
    def programas(self):
        #crador de mp3
        self.idioma=self.barra.get()
        self.locutor=gTTS(self.gtexto,lang=self.idioma)
        self.locutor.save(f'almacen/{self.guardado}.mp3')
        self.inport.ejecucion(self)

    def ejecucion(self):
        self.doc=open('init.bat','w')
        self.doc.write(f'start almacen/{self.guardado}.mp3')
        self.doc.close()
        #iniciador
        self.Os=os
        self.Os.startfile('init.bat')


if __name__=='__main__':
    root=Tk()
    iniciador=ventana(root)
    root.mainloop()

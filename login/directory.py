from tkinter import *
from tkinter.font import*
import webbrowser



class login():
    def __init__(self,ven):
        self.ventana=ven
        self.ventana.title("login")

        #marco1
        self.marco1=Frame(ven,width=400,height=300,bg="deep sky blue")
        self.marco1.pack()
        self.marco1.propagate(0)
        #marco2
        self.marco2=Frame(self.marco1,width=370,height=270)
        self.marco2.propagate(0)
        self.marco2.pack()

        #variables
        self.login=StringVar
        self.pas=StringVar
        self.fuente=Font(family="Lucia Grande",size=14)
        #barra de entrada del login
        self.cadena1=Label(self.marco2,text="login",font=self.fuente)
        self.cadena1.pack()
        self.cadena1.place(x=40,y=30)

        self.entrada1=Entry(self.marco2,borderwidth=2,relief='solid',textvar=self.login,width=34)
        self.entrada1.pack()
        self.entrada1.place(x=60,y=60)
        #barrra de contraseña
        self.cadena2=Label(self.marco2,text="contraseña",font=self.fuente)
        self.cadena2.pack()
        self.cadena2.place(x=40,y=120)

        self.entrada2=Entry(self.marco2,borderwidth=2,relief='solid',textvar=self.pas,show="*",width=34)
        self.entrada2.pack()
        self.entrada2.place(x=60,y=150)

        #boton de salir
        self.botonexi=Button(self.marco2,text="salir",fg='white',bg='red',command=self.quit)
        self.botonexi.pack()
        self.botonexi.place(x=200,y=200)

        #boton de registro
        self.botonref=Button(self.marco2,text="registro",command=self.reg)
        self.botonref.pack()
        self.botonref.place(x=290, y=200)

        #boton de facebook
        self.botonface=Button(self.marco2,text="facebook",fg='white',bg='blue',command=self.facebook)
        self.botonface.pack()
        self.botonface.place(x=235,y=235)
        import guardado
        guardado()

    #definiciones
    def quit(self):
        self.quit=exit()
    def reg(self):
        from ventana import registro
        registro()
    def facebook(self):
        self.url= webbrowser.open('http://www.facebook.com')



roo=Tk()
ve=login(roo)
roo.mainloop()
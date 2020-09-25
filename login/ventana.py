from tkinter import *
from tkinter.font import *



inicio="inicio"
class registro():
	def __init__(self,inicio):

		self.ventana=inicio
		#marco
		self.marco1=Frame(inicio,width=400,height=400,bg="red")
		self.marco1.propagate(0)
		self.marco1.pack()

		#marco2
		self.marco2=Frame(self.marco1,width=360,height=360)
		self.marco2.propagate(0)
		self.marco2.pack()
		#variables
		self.fuente=Font(family="Lucia Grande",size=20)
		self.fuente2=Font(family="Lucia Grande",size=14)
		self.nombre=StringVar
		self.apel=StringVar
		self.edad=StringVar
		self.log=StringVar
		self.con1=StringVar
		self.con2=StringVar

		#barra de titulo
		self.titulo=Label(self.marco2,text="REGISTRO",font=self.fuente)
		self.titulo.pack()

		#barra de nombre
		self.nombre=Label(self.marco2,text="nombre",font=self.fuente2)
		self.nombre.pack()
		self.nombre.place(x=10,y=40)

		self.entrada1=Entry(self.marco2,textvar=self.nombre)
		self.entrada1.pack()
		self.entrada1.place(x=70,y=40)
		#barra de apellido
		self.apellido = Label(self.marco2, text="apellido", font=self.fuente2)
		self.apellido.pack()
		self.apellido.place(x=10, y=60)

		self.entrada2 = Entry(self.marco2, textvar=self.apel)
		self.entrada2.pack()
		self.entrada2.place(x=70,y=70)

		#barra de edad
		self.edad = Label(self.marco2, text="edad", font=self.fuente2)
		self.edad.pack()
		self.edad.place(x=15,y=90)

		self.entrada3 = Entry(self.marco2, textvar=self.edad)
		self.entrada3.pack()
		self.entrada3.place(x=70,y=100)
		#barra de login
		self.login = Label(self.marco2, text="login", font=self.fuente2)
		self.login.pack()
		self.login.place(x=15,y=120)

		self.entrada4 = Entry(self.marco2, textvar=self.log)
		self.entrada4.pack()
		self.entrada4.place(x=70,y=130)
		#barra de pasword
		self.pasword = Label(self.marco2, text="contraseña", font=self.fuente2)
		self.pasword.pack()
		self.pasword.place(x=15, y=150)

		self.entrada5 = Entry(self.marco2, textvar=self.con1,show="*")
		self.entrada5.pack()
		self.entrada5.place(x=70, y=180)

		#barra de comprobacion
		self.pasw = Label(self.marco2, text="confirmacion de contraseña", font=self.fuente2)
		self.pasw.pack()
		self.pasw.place(x=15, y=200)

		self.entrada6 = Entry(self.marco2, textvar=self.con2,show="*")
		self.entrada6.pack()
		self.entrada6.place(x=70, y=220)

		#boton de confirmar
		self.confirmar=Button(self.marco2,text="confirmar",command=self.confirmar)
		self.confirmar.pack()
		self.confirmar.place(x=80,y=260)
		
		#botond de quitar
		self.quitar=Button(self.marco2,text="salir",command=self.quit)
		self.quitar.pack()
		self.quitar.place(x=160,y=260)

	#definiciones
	def guardado(self):
		pass

	def confirmar(self):
		from libreria import funcion
		funcion.ComNombre(self)
		funcion.Comlogin(self)

	def quit(self):
		self.quit=exit()



from ejecutor import Eventana
Eventana()






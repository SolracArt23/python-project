from tkinter import *
class funcion():
    def ComNombre(self):

        from ventana import registro
        registro.guardado(self)
        self.persona1=[]
        self.d=True
        if self.entrada1.get() != '':
            self.persona1.append(self.entrada1.get())
            if self.entrada2.get() != '':
                self.persona1.append(self.entrada2.get())
                if self.entrada3.get() != '':
                    self.persona1.append(self.entrada3.get())
                    from ejecutor import data
                    data.login(self)
                    self.libreriapers=','.join(self.persona1)
                    self.guardadar.write(self.libreriapers)
                    from ejecutor import data
                    data.cerrar(self)




    def Comlogin(self):
        from ventana import registro
        registro.guardado(self)
        self.persona2={}
        if self.entrada4.get()!="":
            self.login=self.entrada4.get()
            if self.entrada5.get()!='':
                self.guardado1=len(self.entrada5.get())
                print(self.guardado1)
                if self.entrada6.get()!='':
                    self.guardado2 = len(self.entrada6.get())
                    self.pasword=self.entrada6.get()

                    if self.guardado1 >=8:
                        print('funciona')
                        self.contraseña=self.entrada6.get()
                        self.persona2.update({self.login:self.pasword})
























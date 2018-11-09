class Empleado(object):# creamso la clase padre Empelado
        """docstring for ClassName"""
        def __init__(self):# constructor 
                self.nombre=""
                self.apellido=""
                self.cedula=""
                self.comisionFija=0.0
        #definimos un agregar y obtener por cada atributo
        def agregarNombre(self, nombre):
                self.nombre=nombre

        def obtenerNombre(self):
                return self.nombre

        def agregarApellido(self,apellido):
                self.apellido=apellido

        def obtenerApellido(self):
                return self.apellido

        def agregarCedula(self,cedula):
                self.cedula=cedula

        def obtenerCedula(self):
                return self.cedula

        def agregarComisionFija(self,comisionFija):
                self.comisionFija=comisionFija

        def obtenerComisionFija(self):
                return self.comisionFija

        def presentarDatos(self):#metodo para impimir el nombre apellido y numeor de cedula de un empleado devuelve todoe n una cadena
                cadena="Informacion de %s %s \n\tCedula: %s"%(self.obtenerNombre(),self.obtenerApellido(),self.obtenerCedula())
                return cadena
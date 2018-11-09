class Empleado(object):
        """docstring for ClassName"""
        def __init__(self):
                self.nombre=""
                self.apellido=""
                self.cedula=""
                self.comisionFija=""
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

        def presentarDatos(self):
                cadena="Informacion de %s %s \n\tCedula: %s"%(self.obtenerNombre(),self.obtenerApellido(),self.obtenerCedula())
                return cadena
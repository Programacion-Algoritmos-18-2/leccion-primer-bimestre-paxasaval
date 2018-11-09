from mipaquete.Empleado import *
class EmpleadoxHoras(Empleado):
	"""docstring for ClassName"""
	def __init__(self):
		super(EmpleadoxHoras, self).__init__()
		self.numeroHoras=0
		self.valorporHora=0.0
		self.sueldo=0.0
	
	#Creamso un aagregar y un obtener por cada atributo no heredado del padre	
	def agregarNumHoras(self,h):
		self.numeroHoras=h

	def obtenerNumHoras(self):
		return self.numeroHoras

	def agregarValorporHora(self, x):
		self.valorporHora=x

	def obtenerValorporHora(self):
		return self.valorporHora

	def calcularSueldo(self):
		self.sueldo=((float(self.obtenerNumHoras())*self.obtenerValorporHora())+super(EmpleadoxHoras,self).obtenerComisionFija())
		return self.sueldo

	def presentarDatos(self):
		cadena="%s\nNumero de horas: %d\nValor de la hora. %.2f\nSueldo Final: %.2f\n"%(super(EmpleadoxHoras,self).presentarDatos(),self.obtenerNumHoras(),self.obtenerValorporHora(),self.calcularSueldo())
		return cadena
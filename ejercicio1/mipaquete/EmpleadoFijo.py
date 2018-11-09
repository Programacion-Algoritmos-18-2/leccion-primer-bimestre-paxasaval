from mipaquete.Empleado import *
class EmpleadoFijo(Empleado):
	"""docstring for ClassName"""
	def __init__(self):
		super(EmpleadoFijo, self).__init__()# heredamos loa atruibutos del padre EMpleado
		self.descuento_seguro=0.0
		self.sueldo_fijo=0.0
		self.sueldo_final=0.0
	#Creamso un aagregar y un obtener por cada atributo no heredado del padre
	def agregardescuentoSeguro(self,desc):
		self.descuento_seguro=desc/100

	def obtenerdescuentoSeguro(self):
		return self.descuento_seguro

	def agregarsueldoFijo(self, x):
		self.sueldo_fijo=x

	def obtenersueldoFijo(self):
		return self.sueldo_fijo

	def calcularSueldo(self):
		self.sueldo_final=(self.obtenersueldoFijo()-(self.obtenerdescuentoSeguro()*self.obtenersueldoFijo()))+super(EmpleadoFijo,self).obtenerComisionFija()
		return self.sueldo_final

	def presentarDatos(self):#a al cadena del padre le agregamos los nuevos atributos y todo lo encansulamso en una cadena 
		cadena="%sSueldo Fijo: %.2f\nDescuento:  %.2f\nSueldo Final: %.2f\n"%(super(EmpleadoFijo,self).presentarDatos(),self.obtenersueldoFijo(),self.obtenerdescuentoSeguro(),self.calcularSueldo())
		return cadena
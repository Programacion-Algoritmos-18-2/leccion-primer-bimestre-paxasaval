from mipaquete.Empleado import *
class EmpleadoxSemana(Empleado):
	"""docstring for ClassName"""
	#constructor
	def __init__(self):
		super(EmpleadoxSemana, self).__init__()# heredamos loa atruibutos del padre EMpleado
		self.num_semanas=0
		self.valorxsemana=0.0
		self.sueldo_final=0.0
	#por cada atributo no heredado del padre creamso un agregar y un obtener
	def agregarnumSemanas(self,n):
		self.num_semanas=n

	def obtenernumSemanas(self):
		return self.num_semanas

	def agregarValorxSemana(self, x):
		self.valorxsemana=x

	def obtenerValorxSemana(self):
		return self.valorxsemana

	def calcularSueldo(self):
		self.sueldo_final=(self.obtenernumSemanas()*self.obtenerValorxSemana())+(super(EmpleadoxSemana,self).obtenerComisionFija())
		return self.sueldo_final

	def presentarDatos(self):#a al cadena del padre le agregamos los nuevos atributos y todo lo encansulamso en una cadena 
		cadena="%sSueldo por Semana: %.2f\nNumero de Semanas:  %.2f\nSueldo Final: %.2f\n"%(super(EmpleadoxSemana,self).presentarDatos(),self.obtenerValorxSemana(),self.obtenernumSemanas(),self.calcularSueldo())
		return cadena
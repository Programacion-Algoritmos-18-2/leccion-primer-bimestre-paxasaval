#Importaciond de las clases
from mipaquete.Empleado import *
from mipaquete.EmpleadoxHoras import *
from mipaquete.EmpleadoFijo import *
from mipaquete.EmpleadoxSemana import *
#Objeto 1 Empleado
e=Empleado()#Crear el objeto en vacio
e.agregarNombre("Luis")#Actualizamos el nombre
e.agregarApellido("Benitez")# Actualizamos el Apellido
e.agregarCedula("11110001")#Actualizamos la cedula
print(e.presentarDatos())#Imprimimos el priemr objeto
#Objeto 2 Empleado x horas
e1=EmpleadoxHoras()
nombre=input("Ingrese su nombre: ")#pedimso el usuario el bnombre
e1.agregarNombre(nombre)# lo actualizamso object 2
e1.agregarApellido("Andrade")
e1.agregarCedula("112233")
e1.agregarValorporHora(20.2)
e1.agregarNumHoras(15)
print(e1.presentarDatos())#Imprimimos el Objeto 2
#Objeto 3 Empleado Fijo
e2=EmpleadoFijo()#creamos objeto 3 
e2.agregarsueldoFijo(300.2)
e2.agregardescuentoSeguro(10)
comision=float(input("Ingrese la comision: "))
e2.agregarComisionFija(comision)
e2.nombre=("Ana")
e2.apellido=("Diaz")
print(e2.presentarDatos())# imprimimos objeto 3
#Objeto 4 Empleado x Semanas
e3=EmpleadoxSemana()# creamso el objeto 4
e3.agregarnumSemanas(10)
e3.agregarValorxSemana(25.0)
print(e3.presentarDatos())#impimimos objeto 4
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicio1.java;

/**
 *
 * @author Salas
 */
public class EmpleadoFijo extends Empleado{
    public double sueldo_fijo,descuento_seguro;
    public double sueldo_final;

    public EmpleadoFijo(double sueldo_fijo, int descuento_seguro, String nombre, String apellido, String cedula, double comision_fija) {
        super(nombre, apellido, cedula, comision_fija);
        this.sueldo_fijo = sueldo_fijo;
        this.descuento_seguro = (double)descuento_seguro/100;
    }

    public double getSueldo_fijo() {
        return sueldo_fijo;
    }

    public void setSueldo_fijo(double sueldo_fijo) {
        this.sueldo_fijo = sueldo_fijo/100;
    }

    public double getDescuento_seguro() {
        return descuento_seguro;
    }

    public void setDescuento_seguro(int descuento_seguro) {
        this.descuento_seguro = (double)descuento_seguro/100;
    }
    public double calcularSueldo(){
        this.sueldo_final=(this.sueldo_fijo-(this.sueldo_fijo*this.descuento_seguro));
        return this.sueldo_final;
    }
    @Override
    public String toString(){
        String cadena=String.format("%s\nSueldo FIjo: %.2f\nDescuento: %.2f\nSueldo Final: %.2f",super.toString(),getSueldo_fijo(),getDescuento_seguro(),calcularSueldo());
        return cadena;
    }

    
}

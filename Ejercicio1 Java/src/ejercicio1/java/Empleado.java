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
public class Empleado {
    private String nombre,apellido,cedula;
    private double comision_fija;

    public Empleado(String nombre, String apellido, String cedula, double comision_fija) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.cedula = cedula;
        this.comision_fija = comision_fija;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getCedula() {
        return cedula;
    }

    public void setCedula(String cedula) {
        this.cedula = cedula;
    }

    public double getComision_fija() {
        return comision_fija;
    }

    public Empleado() {
    }

    public void setComision_fija(double comision_fija) {
        this.comision_fija = comision_fija;
    }
    
    @Override
    public String toString(){
        String cadena=String.format("Informacion de %s %s\n\tCedula: %s\n",getNombre(),getApellido(),getCedula());
        return cadena;
    }
}

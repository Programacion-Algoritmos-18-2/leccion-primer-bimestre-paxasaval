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
public class EmpleadoxSemanas extends Empleado {

    public int numSemanas;
    public double valorSemana1;
    public double sueldo;

    public EmpleadoxSemanas(int numSemanas, double valorSemana1, String nombre, String apellido, String cedula, double comision_fija) {
        super(nombre, apellido, cedula, comision_fija);
        this.numSemanas = numSemanas;
        this.valorSemana1 = valorSemana1;
    }

    public int getNumSemanas() {
        return numSemanas;
    }

    public void setNumSemanas(int numSemanas) {
        this.numSemanas = numSemanas;
    }

    public double getValorSemana1() {
        return valorSemana1;
    }

    public void setValorSemana1(double valorSemana1) {
        this.valorSemana1 = valorSemana1;
    }
    public double calcularSueldo(){
        this.sueldo=(this.numSemanas*this.valorSemana1)+super.getComision_fija();
        return this.sueldo;
    }
    
    @Override
    public String toString() {
        String cadena = String.format("%s\nNumero de Semanas: %d\nValor por Semana: %.2f\nSueldo Final: %.2f", super.toString(), getNumSemanas(), getValorSemana1(), calcularSueldo());
        return cadena;
    }
}

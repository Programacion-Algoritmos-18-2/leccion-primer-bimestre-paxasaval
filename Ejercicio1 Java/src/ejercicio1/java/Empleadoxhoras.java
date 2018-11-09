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
public class Empleadoxhoras extends Empleado {

    private int num_horas;
    private double valorHora, sueldo;

    public Empleadoxhoras(int num_horas, double valorHora, double sueldo, String nombre, String apellido, String cedula, double comision_fija) {
        super(nombre, apellido, cedula, comision_fija);
        this.num_horas = num_horas;
        this.valorHora = valorHora;
        this.sueldo = sueldo;
    }

    public int getNum_horas() {
        return num_horas;
    }

    public void setNum_horas(int num_horas) {
        this.num_horas = num_horas;
    }

    public double getValorHora() {
        return valorHora;
    }

    public void setValorHora(double valorHora) {
        this.valorHora = valorHora;
    }

    public double obtenerSueldo() {
        this.sueldo = (this.num_horas * this.valorHora) + super.getComision_fija();
        return this.sueldo;
    }

    @Override
    public String toString() {
        String cadena = String.format("%s\nNumero de horas: %d\nValor de cada Hora: %.2f\nSueldo Final: %.2f", super.toString(), getNum_horas(), getValorHora(), obtenerSueldo());
        return cadena;
    }
}

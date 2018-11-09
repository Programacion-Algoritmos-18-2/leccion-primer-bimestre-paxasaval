/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejercicio1.java;

import java.util.Scanner;

/**
 *
 * @author Salas
 */
public class Ejercicio1Java {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner entrada=new Scanner(System.in);
        Empleado e=new Empleado("Luis","Benitez","1110001",0.0);
        Empleadoxhoras e1;
        System.out.println(e.toString());
        System.out.println("Ingrese el nombre");
        String nombre=entrada.nextLine();
        e1= new Empleadoxhoras(15,20.2,0.0,nombre,"","",0.0);
        e1.setApellido("Benitez");
        e1.setCedula("1110001");
        System.out.println(e1.toString());
        EmpleadoFijo e2=new EmpleadoFijo(300.2,10,"Luis","Benitez","1110001",0.0);
        System.out.println(e2.toString());
    }
    
}

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Salário do funcionário: ");
        float salario = teclado.nextFloat();
        double novosalario = salario + salario * 15 / 100;
        System.out.println("Um funcionário que recebia "+salario+" com o aumento de 15% passará a receber "+novosalario);
    }
}
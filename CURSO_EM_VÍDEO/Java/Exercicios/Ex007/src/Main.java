import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("Calcule a média dos Alunos abaixo:");
        System.out.println(" ");
        System.out.print("Primeira nota: ");
        float n1 = teclado.nextFloat();
        System.out.print("Segunda nota: ");
        float n2 = teclado.nextFloat();
        float m = (n1 + n2) / 2;
        System.out.print("A média do aluno que tirou as notas "+n1 +" e "+ n2+ " é igual a " +m);
    }
}
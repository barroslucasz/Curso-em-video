import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Primeira nota: ");
        float n1 = teclado.nextFloat();
        System.out.print("Segunda nota: ");
        float n2 = teclado.nextFloat();
        float m = (n1+n2) /2 ;
        System.out.println("Sua média foi "+m);
        if (m>7) {
            System.out.println("Parabéns!");
        }
        // --------------------------------------

        Scanner t = new Scanner(System.in);
        System.out.print("Digite seu ano de nascimento: ");
        int idade = t.nextInt();
        int i = 2023 - idade;
        System.out.println("Sua idade é "+i);
        if (i>=18){
            System.out.println("Você é maior de idade.");
        }else {
            System.out.println("Você é menor de idade.");
        }

    }
}
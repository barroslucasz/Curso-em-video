import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int n = teclado.nextInt();
        System.out.println("Analisando o número "+n+" Temos: ");
        int u = n / 1 % 10;
        int d = n / 10 % 10;
        int c = n / 100 % 10;
        int m = n / 1000 % 10;
        System.out.println("Unidade: "+u);
        System.out.println("Dezena: "+d);
        System.out.println("Centena: "+c);
        System.out.println("Milhar: "+m);
    }
}
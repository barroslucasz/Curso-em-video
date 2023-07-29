import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int n = teclado.nextInt();
        int d = n + n;
        int t = n + n + n;
        double r = Math.sqrt(n);
        System.out.printf("O dobro de %d é %d%n", n, d);
        System.out.printf("O triplo de %d é %d%n", n, t);
        System.out.printf("A raiz quadrada de %d é %.0f%n", n, r);
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um número: ");
        int num = teclado.nextInt();
        System.out.println("Analisando o número " + num + " Seu Antecessor é " + (num-1) + " e seu Sucessor é " + (num+1));
    }
}
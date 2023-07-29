import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("");
        System.out.println("-=-=-= CONVERSOR DE REAL PARA DÓLAR -=-=-=");
        System.out.println("");
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite um valor em Real: ");
        float real = teclado.nextFloat();
        double dolar = real / 4.73;
        System.out.println(real+" Reais você consegue comprar "+dolar);

    }
}
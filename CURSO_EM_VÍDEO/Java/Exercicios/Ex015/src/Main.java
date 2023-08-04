import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Quantos dias alugado: ");
        int dias = teclado.nextInt();
        System.out.print("Quantos KM rodados: ");
        float distancia = teclado.nextFloat();
        int tdias = dias*60;
        double kmr = distancia*0.15;
        System.out.println("O total a pagar é R$: "+(tdias+kmr));

    }
}
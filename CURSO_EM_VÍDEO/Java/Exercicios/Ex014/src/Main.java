import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Informe a temperatura em ºC: ");
        float celsius = teclado.nextFloat();
        double fire = celsius * 9 / 5 + 32;
        System.out.println("A temperatura de "+celsius+"ºC corresponde a "+fire+"ºF");
    }
}
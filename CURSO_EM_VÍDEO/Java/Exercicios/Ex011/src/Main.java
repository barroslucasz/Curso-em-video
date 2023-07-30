import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite a largura: ");
        float largura = teclado.nextFloat();
        System.out.print("Digite a altura: ");
        float altura = teclado.nextFloat();
        float area = largura*altura;
        float tinta = (largura*altura)/2;
        System.out.println("Sua parede tem dimensões de "+largura+ "X"+altura+"e sua área é de "+area+"m²");
        System.out.println("Para pintar sua parede, você precisará de "+tinta+"l de tinta.");

    }
}
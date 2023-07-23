import java.util.Scanner;

public class TiposPrimitivos{

    public static void main(String[] args) {

        try (Scanner teclado = new Scanner(System.in)) {
            System.out.printf("Digite um nome: ");
            String nome = teclado.nextLine();

            System.out.printf("Digite uma nota: ");
            float nota = teclado.nextFloat();

            System.out.printf("A nota de %s é %.2f", nome, nota);
        }
        
}
    }
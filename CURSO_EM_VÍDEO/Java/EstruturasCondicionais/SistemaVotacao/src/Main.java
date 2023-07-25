import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("-=-=-= VERIFICADOR DE OBRIGATORIEDADE DE VOTAÇÃO -=-=-=");
        System.out.println("");
        System.out.print("Digite sua idade: ");
        int idade = teclado.nextInt();
        if (idade>=18){
            System.out.println("Voce tem voto OBRIGATÓRIO!");
        } else if (idade<16) {
            System.out.println("Seu voto NÃO É OBRIGATÓRIO!");
        } else if (idade>=70) {
            System.out.println("Seu voto NÃO É OBRIGATÓRIO!");
        }

    }
}
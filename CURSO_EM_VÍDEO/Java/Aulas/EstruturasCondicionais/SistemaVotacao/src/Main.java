import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        System.out.println("-=-=-= VERIFICADOR DE OBRIGATORIEDADE DE VOTAÇÃO -=-=-=");
        System.out.println("");
        System.out.print("Digite sua idade: ");
        int ano = teclado.nextInt();
        int idade = 2023 - ano;
        if (idade <16){
            System.out.println("Proibido Votar com "+idade);
        }
        else {
            if ((idade>=16 && idade <18) || (idade>70)){
                System.out.println("Voto opcional com "+idade);
            }
            else {
                System.out.println("Voto Obrigatório com "+idade);
            }
        }
    }
}
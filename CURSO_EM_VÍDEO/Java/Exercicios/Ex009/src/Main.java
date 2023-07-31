import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("");
        System.out.println("-=-=-= TABUADA -=-=-=");
        System.out.println(" ");

        System.out.print("Digite um número para ver sua tabuada: ");
        Scanner teclado = new Scanner(System.in);
        int tabuada = teclado.nextInt();

        int x1 = tabuada * 1;
        int x2 = tabuada *2;
        int x3 = tabuada *3;
        int x4 = tabuada *4;
        int x5 = tabuada *5;
        int x6 = tabuada *6;
        int x7 = tabuada *7;
        int x8 = tabuada *8;
        int x9 = tabuada *9;
        int x10 = tabuada *10;

        System.out.println("A tabuada de "+tabuada +" é:");
        System.out.println(tabuada+ "X1 = " +x1);
        System.out.println(tabuada+ "X2 = "+x2);
        System.out.println(tabuada+ "X3 = "+x3);
        System.out.println(tabuada+ "X4 = "+x4);
        System.out.println(tabuada+ "X5 = "+x5);
        System.out.println(tabuada+ "X6 = "+x6);
        System.out.println(tabuada+ "X7 = "+x7);
        System.out.println(tabuada+ "X8 = "+x8);
        System.out.println(tabuada+ "X9 = "+x9);
        System.out.println(tabuada+ "X10 = "+x10);
    }
}
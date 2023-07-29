import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println(" ");
        System.out.println("Conversor de METROS em outras unidades de medida");
        Scanner teclado = new Scanner(System.in);
        System.out.println("");

        System.out.print("Digite uma medida em Metros: ");
        float medida = teclado.nextFloat();
        float dam = medida / 10;
        float hm = medida / 100;
        float km = medida / 1000;
        float dm = medida * 10;
        float cm = medida * 100;
        float mm = medida * 1000;
        System.out.println("A medida de "+medida+ "m é igual a:");
        System.out.println(km+" km");
        System.out.println(hm+" hm");
        System.out.println(dam+" dam");
        System.out.println(dm+" dm");
        System.out.println(cm+ " cm");
        System.out.println(mm+ "mm");
    }
}
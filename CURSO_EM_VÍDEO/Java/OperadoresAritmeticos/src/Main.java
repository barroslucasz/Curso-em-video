public class Main {

    public static void main(String[] args) {
        System.out.println("Olá, Mundo");
        // OPERAÇÃO NORMAL COM ORDEM DE PRECEDENCIA
        int n1 = 3;
        int n2 = 5;
        float m = (n1+n2) / 2;
        System.out.println("A média é igual a " + m);
        System.out.println("");

        // OPERADORES UNARIOS
        int numero = 10;
        int valor = 4 + numero++;

        System.out.println(valor);
        System.out.println(numero);
        System.out.println("");

        // OPERADORES DE ATRIBUIÇÃO
        int x = 4;
        x += 2; // x = x+2 isso pode ser para qualquer calculo
        System.out.println(x);
        System.out.println("");

        // CLASS MATH
        int teste = (int) Math.pow(5,2);
        int teste1 = (int) Math.sqrt(25);
        System.out.println(teste);
        System.out.println(teste1);
        System.out.println("");

        // ARRENDONDAMENTOS

        // para baixo usamos o floor (que na minha opnião ele elimina o decimal)
        float v = 8.3f;
        int arren =(int) Math.floor(v);
        System.out.println(arren);

        int teste2 = (int) Math.floor(8.3); // POSSO USAR DESTE METODO
        System.out.println(teste2);

        // para cima usamos o ceil
        float a = 8.3f;
        int ar = (int) Math.ceil(a);
        System.out.println(ar);

        int b = (int) Math.ceil(8.3); // MANEIRA COM MENOS LINHA
        System.out.println(b);

        // para arrendondamento aritimetrico usamos round
        float c = 8.4f;
        int arr = Math.round(c);
        System.out.println(arr);
        System.out.println("");

        // GERADORES DE NUMERO
        double ale = Math.random();
        int n = (int) (5 + ale *(10-5)); // isso tudo para poder gerar um numero entre 5 e 10
        System.out.println(n);
    }
}
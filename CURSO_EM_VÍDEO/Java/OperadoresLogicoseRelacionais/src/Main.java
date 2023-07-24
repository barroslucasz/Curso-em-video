public class Main {
    public static void main(String[] args) {
        int n1, n2, r;
        n1 = 4;
        n2 = 8;
        r = (n1>n2)?n1:n2;
        System.out.println(r);
        System.out.println("");

        // comparação de str

        String nome1 = "Lucas";
        String nome2 = "Lucas";
        String nome3 = new String("Lucas");
        String res;
        res = (nome1.equals(nome3))?"Igual":"Diferente";
        System.out.println(res);
        System.out.println("");

        // operadores logicos
        int x, y, z;
        x = 4;
        y = 7;
        z = 12;
        boolean re;
        re = (x<y || y==z)?true:false;
        System.out.println(re);

    }
}
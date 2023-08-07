import java.util.Arrays;

public class Main03 {
    public static void main(String[] args) {
        int num[] = {5,4,8,9,1,3,7};
        Arrays.sort(num);
        for(int valor: num){
            System.out.print(valor+ " ");
        }
    }
}

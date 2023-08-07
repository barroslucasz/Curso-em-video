import java.util.Arrays;

public class Main04 {
    public static void main(String[] args) {
        int vet[] = {3,7,6,1,9,4,2};
        for (int v:vet){
            System.out.print(v+ " ");
        }
        int p = Arrays.binarySearch(vet, 1);
        System.out.println("Encontrei o valor na posição "+ p);
    }
}

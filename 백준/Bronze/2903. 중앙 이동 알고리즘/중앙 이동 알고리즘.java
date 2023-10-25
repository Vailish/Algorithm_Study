import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num=2;
        for (int i=0; i<n; i++) {
            num += Math.pow(2, i);
        }
        System.out.println(num * num);
    }
}

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int num = 1;

        while (n > 1) {
            num++;
            if (n % num==0) {
                System.out.println(num);
                n /= num;
                num = 1;
            }
        }
    }
}

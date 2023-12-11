import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < n; i++) {
            BigInteger num = sc.nextBigInteger();
            answer.append(chk(num)).append("\n");
        }
        System.out.println(answer);
    }

    static BigInteger chk(BigInteger n) {
        if (n.isProbablePrime(10) == true) {
            return n;
        } else {return n.nextProbablePrime();}
    }
}
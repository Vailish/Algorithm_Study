import java.util.Scanner;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String st = sc.next();
        int idx = 0;
        while (idx < st.length()) {
            System.out.println(st.charAt(idx));
            idx++;
        }
    }
}
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] texts = sc.nextLine().toCharArray();
        StringBuilder answer = new StringBuilder();
        
        int idx = 0;
        while (idx < texts.length) {
            if (Character.isUpperCase(texts[idx])) {
                answer.append(Character.toLowerCase(texts[idx]));
            } else {
                answer.append(Character.toUpperCase(texts[idx]));
            }
            idx++;
        }
        System.out.println(answer);
    }
}
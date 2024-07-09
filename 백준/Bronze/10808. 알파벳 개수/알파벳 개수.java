import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // a = 97
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String words = br.readLine();
        int[] cnt = new int[26];

        for (int i=0; i<words.length(); i++) {
            cnt[words.charAt(i)-97]++;
        }
        StringBuilder answer = new StringBuilder();
        for (int i=0; i<26; i++) {
            answer.append(cnt[i]).append(" ");
        }
        System.out.println(answer);
    }
}
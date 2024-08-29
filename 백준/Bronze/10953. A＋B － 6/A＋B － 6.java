import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder answer = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i<T; i++) {
            String[] nums = br.readLine().split(",");
            answer.append(Integer.parseInt(nums[0]) + Integer.parseInt(nums[1])).append("\n");
        }
        System.out.println(answer);
    }
}

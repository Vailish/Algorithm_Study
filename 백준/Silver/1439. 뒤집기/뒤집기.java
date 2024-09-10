import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String nums = br.readLine();

        // 0 -> 0으로 변환 횟수, 1 -> 1으로 변환 횟수
        int[] result = new int[2];
        boolean isChange = false;

        char exNum = nums.charAt(0);
        char nowNum;

        result[exNum-'0']++;

        // 연속된 녀석들을 하나로 묶어서 카운트
        for (int i=0; i<nums.length(); i++) {
            nowNum = nums.charAt(i);
            if (exNum != nowNum) {
                exNum = nowNum;
                // result 채워넣기
                result[exNum - '0']++;
                isChange = true;
            }
        }
        if (!isChange) {
            System.out.println(0); return;
        }
        int answer;
        if (result[0]==0) {
            answer = result[1];
        } else if (result[1]==0) {
            answer = result[0];
        } else {
            answer = Math.min(result[0], result[1]);
        }
        System.out.println(answer);
    }
}
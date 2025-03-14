import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = Arrays.copyOf(arr, arr.length);
        for (int[] query : queries) {
            for (int i=query[0]; i<=query[1]; i++) {
                answer[i]++;
            }
        }
        return answer;
    }
}
import java.util.Arrays;

class Solution {
    public int[] solution(int[] arr) {
        int cnt = 0;
        boolean isFirst = true;
        int startIdx = 100000;
        int endIdx = 0;
        // 2 확인
        for (int i=0; i<arr.length; i++) {
            if (arr[i] == 2) {
                cnt++;
                if (isFirst) {
                    startIdx = i;
                    isFirst=false;
                }
                endIdx = i;
            }
        }
        
        if (cnt == 0) { // 2가 없으면 -1 반환
            return new int[]{-1};
        } else { // 2가 하나 이상이면 범위 반환
            return Arrays.copyOfRange(arr, startIdx, endIdx + 1);
        }
    }
}
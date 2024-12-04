import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> result = new ArrayList<>();
        for (String intStr : intStrs) {
            int idx = 0;
            int num = Integer.parseInt(intStr.substring(s, s+l));
            if (num > k) {
                result.add(num);
            }
        }
        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}
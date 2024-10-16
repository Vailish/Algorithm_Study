import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        int[] answer = {-1};
        List<Integer> result = new ArrayList<>();
        for (int i=l; i<=r; i++) {
            if (i%5==0) {
                String num = String.valueOf(i);
                int cnt=0;
                for (int j=0; j<num.length(); j++) {
                    if (num.charAt(j)=='5' || num.charAt(j)=='0') cnt++;
                }
                if (cnt == num.length()) result.add(Integer.parseInt(num));
            }
        }
        if (result.size()>0) {
            answer = result.stream().mapToInt(Integer::intValue).toArray();
        }
            
            
            
        return answer;
    }
}
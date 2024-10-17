import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        List<Integer> result = new ArrayList<>();
        while (n > 1) {
            result.add(n);
            if (n%2==0) {
                n = n/2;
            } else {
                n=3*n+1;
            }
        }
        result.add(1);
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}
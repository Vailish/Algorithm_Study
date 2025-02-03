import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        List<Integer> tmp = new ArrayList<Integer>();
        for (int[] idx : intervals) {
            for (int i=idx[0]; i<=idx[1]; i++) {
                tmp.add(arr[i]);
            }
        }
        
        return tmp.stream().mapToInt(Integer::intValue).toArray();
    }
}
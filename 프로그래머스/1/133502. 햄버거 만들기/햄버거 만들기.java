import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack stack = new Stack<Integer>();
        
        for (int num : ingredient) {
            stack.push(num);
            
            int s = stack.size();
            if (s >= 4
                && stack.get(s-4).equals(1)
                && stack.get(s-3).equals(2)
                && stack.get(s-2).equals(3)
                && stack.get(s-1).equals(1)) {
                answer ++;
                for (int i=0;i<4;i++) {stack.pop();}
            }
        }
        
        return answer;
    }
}
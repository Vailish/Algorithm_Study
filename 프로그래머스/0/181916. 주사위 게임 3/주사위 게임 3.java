import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] chk = {a, b, c, d};
        Arrays.sort(chk);
        
        Set<Integer> set = new HashSet<>();
        set.add(a);
        set.add(b);
        set.add(c);
        set.add(d);
        
        switch (set.size()) {
            case 1: answer = 1111*a; break;
            case 2: 
                // 2, 2 인 경우
                if (chk[0]==chk[1] && chk[2]==chk[3]) {
                    answer = (chk[0] + chk[3]) * (chk[3]-chk[0]);
                } else {
                    answer = (chk[0] == chk[1])
                            ? (10 * chk[0] + chk[3]) * (10 * chk[0] + chk[3])
                            : (10 * chk[3] + chk[0]) * (10 * chk[3] + chk[0]);
                }
                break;
            case 3: // 2개가 같고 2개가 다른경우
                int[] cntArr = new int[7];
                for (int v : chk) {
                    cntArr[v]++;
                }
                answer = 1;
                for (int i=1; i<cntArr.length; i++) {
                    if (cntArr[i] == 1) answer *= i;
                }
                break;
            case 4: answer = chk[0];
            }
        return answer;
    }
}
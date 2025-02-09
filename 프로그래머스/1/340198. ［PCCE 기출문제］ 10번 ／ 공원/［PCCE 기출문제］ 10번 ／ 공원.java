import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int[] mats, String[][] park) {
        Integer[] sortedMats = Arrays.stream(mats).boxed().toArray(Integer[]::new);
        Arrays.sort(sortedMats, Collections.reverseOrder());
        
        for (int size : sortedMats) {
            for (int i=0; i<=park.length-size; i++) {
                for (int j=0; j<=park[0].length-size; j++) {
                    if (chk(i, j, size, park)) return size;
                }
            }
        }
        return -1;
    }
    
    boolean chk(int i, int j, int size, String[][] map) {
        for (int x=i; x<i+size; x++) {
            for (int y=j; y<j+size; y++) {
                if (!map[x][y].equals("-1")) return false;
            }
        }
        return true;
    }
}
import java.util.Arrays;
class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        String[] st = new String[my_string.length()];
        for (int i=0; i<my_string.length(); i++) {
            st[i] = String.valueOf(my_string.charAt(i));
        }
        
        // query 실행하기
        String tmp;
        for (int[] query : queries) {
            st = reverse(st, query[0], query[1]);
            // System.out.println(Arrays.toString(st));
        }
        
        
        for (String word:st) {
            answer += word;
        }
        return answer;
    }
    // startIdx에서 endIdx까지 뒤집기
    String[] reverse(String[] words, int startIdx, int endIdx) {
        String tmp = "";
        while (startIdx < endIdx) {
            tmp = words[startIdx];
            words[startIdx] = words[endIdx];
            words[endIdx] = tmp;
            startIdx++;
            endIdx--;
        }
        return words;
    }
}
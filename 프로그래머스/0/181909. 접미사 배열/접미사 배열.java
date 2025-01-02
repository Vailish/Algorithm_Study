import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length()];
        for (int i=0; i<my_string.length(); i++) {
            answer[i] = my_string.substring(i);
        }
        Arrays.sort(answer, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                return s1.compareTo(s2); // 기본 문자열 사전순 비교
            }
        });
        return answer;
    }
}
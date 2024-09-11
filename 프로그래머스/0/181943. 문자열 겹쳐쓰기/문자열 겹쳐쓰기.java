class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String head = my_string.substring(0, s);
        String body = overwrite_string;
        String tail = my_string.substring(s+overwrite_string.length());

        String answer = head + body + tail;
        
        return answer;
    }
}
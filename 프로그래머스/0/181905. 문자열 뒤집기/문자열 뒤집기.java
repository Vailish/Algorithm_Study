class Solution {
    public String solution(String my_string, int s, int e) {
        return my_string.substring(0, s) + reverseWord(my_string.substring(s,e+1)) + my_string.substring(e+1);
    }
    String reverseWord(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<word.length(); i++) {
            sb.append(word.charAt(word.length() -i -1));
        }
        return sb.toString();
    }
}
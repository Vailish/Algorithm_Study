class Solution {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        for (char my_char:my_string.toCharArray()) {
            answer[my_char >= 'a' ? my_char - 'a' + 26 : my_char - 'A']++;
        }
        return answer;
    }
}
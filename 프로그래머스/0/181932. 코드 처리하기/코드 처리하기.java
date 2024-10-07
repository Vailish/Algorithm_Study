class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = -1; // -1, 1
        for (int idx = 0; idx < code.length(); idx++) {
            if (mode == -1) {
                if (code.charAt(idx) == '1') {
                    mode *= -1;
                } else {
                    if (idx % 2 == 0) answer += code.charAt(idx);
                }
            } else {
                if (code.charAt(idx) == '1') {
                    mode *= -1;
                } else {
                    if (idx % 2 == 1) answer += code.charAt(idx);
                }
            }
        }
        return answer=="" ? "EMPTY" : answer;
    }
}
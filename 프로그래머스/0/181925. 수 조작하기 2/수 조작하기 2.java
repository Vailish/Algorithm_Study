class Solution {
    public String solution(int[] numLog) {
        StringBuilder answer = new StringBuilder();
        int num = numLog[0];
        for (int i=1; i<numLog.length; i++) {
            String nextWord = "";
            switch (numLog[i] - numLog[i-1]) {
                case 1: nextWord = "w"; break;
                case -1: nextWord = "s"; break;
                case 10: nextWord = "d"; break;
                case -10: nextWord = "a"; break;
            }
            answer.append(nextWord);
        }
        return answer.toString();
    }
}
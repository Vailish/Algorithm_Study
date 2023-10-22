class Solution {
    public int solution(String s) {
        int answer = 0;
        
        char x = s.charAt(0);
        int xNum = 1;
        int otherNum = 0;
        
        for (int i=1; i<s.length(); i++) {
            char targetWord = s.charAt(i);
            
            if (xNum == otherNum) {
                answer += 1;
                xNum = 0;
                otherNum = 0;
                x = targetWord;
            }
            
            if (x == targetWord) {
                xNum += 1;
            } else {
                otherNum += 1;
            }
        
        }
        
        return answer +1;
    }
}
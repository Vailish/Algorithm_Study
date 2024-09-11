class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        int numA = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int numB = Integer.parseInt(String.valueOf(b) + String.valueOf(a));
        
        return Math.max(numA, numB);
    }
}
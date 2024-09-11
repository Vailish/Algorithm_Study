class Solution {
    public int solution(int a, int b) {
        return Math.max(caculate(a, b), 2 * a * b);
    }
    
    static int caculate(int a, int b) {
        return Integer.parseInt(String.valueOf(a)+String.valueOf(b));
    }
}
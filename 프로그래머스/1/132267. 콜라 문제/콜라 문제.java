class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        int q = n;
        int r = 0;
        while (n >= a) {
            q = (int) Math.floor(n / a);
            n = n % a;
            
            answer += q * b;
            n = b*q + n;
            System.out.println(String.format("n : %s answer : %s n+q : %s",n, answer, n+q));
        }
        return answer;
    }
}
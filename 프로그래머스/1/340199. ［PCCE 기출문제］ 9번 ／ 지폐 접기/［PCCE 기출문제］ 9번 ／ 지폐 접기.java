class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        int smallNum = bill[0] > bill[1] ? bill[1] : bill[0];
        int bigNum = bill[0] > bill[1] ? bill[0] : bill[1];
        
        int walletBigNum = wallet[0] > wallet[1] ? wallet[0] : wallet[1];
        int walletSmallNum = wallet[0] > wallet[1] ? wallet[1] : wallet[0];
        
        while (walletSmallNum < smallNum || walletBigNum < bigNum) {
            answer++;
            bigNum = bigNum / 2;
            if (smallNum > bigNum) {
                int tmp = smallNum;
                smallNum = bigNum;
                bigNum = tmp;
            }
        }
        
        return answer;
    }
}
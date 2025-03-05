class Solution {
    public int solution(int[] num_list) {
        int numA = 0;
        int numB = 0;
        for (int i=0; i<num_list.length; i++) {
            if (i%2==0) {
                numA += num_list[i];
            } else {
                numB += num_list[i];
            }
        }
        return numA > numB ? numA : numB;
    }
}
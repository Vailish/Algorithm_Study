class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = arr;
        int tmp; int i; int j;
        for (int[] query : queries) {
            i = query[0]; j = query[1];
            tmp = answer[i];
            answer[i] = answer[j];
            answer[j] = tmp;
        }
        return answer;
    }
}
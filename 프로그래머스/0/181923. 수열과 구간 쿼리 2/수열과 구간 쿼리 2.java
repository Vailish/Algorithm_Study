class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        int minNum; int maxNum; int conNum; int result;
        for (int i=0; i<queries.length; i++) {
            result = 1000001;
            minNum = queries[i][0]; maxNum = queries[i][1]; conNum = queries[i][2];
            
            for (int j=minNum; j<=maxNum; j++) {
                if (arr[j] < result && arr[j] > conNum) result = arr[j];
            }
            if (result > 1000000) result = -1;
            answer[i] = result;
        }  
        return answer;
    }
}
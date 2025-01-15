class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {
        int[] answer = {};
        int a = slicer[0];
        int b = slicer[1];
        int c = slicer[2];
        int k = 0;
        
        switch (n) {
            case 1 : // b번 인덱스 까지
                answer = new int[b+1];
                for (int i=0; i<b+1; i++) {
                    answer[i] = num_list[i];
                }
                break;
            case 2 : // a부터 마지막 인덱스 까지
                answer = new int[num_list.length - a];
                for (int i=a; i<num_list.length; i++) {
                    answer[k++] = num_list[i];
                }
                break;
            case 3 : // a번부터 b번 인덱스 까지
                answer = new int[b-a+1];
                for (int i=a; i<b+1; i++) { // 1 5
                    answer[k++] = num_list[i];
                }
                break;
            case 4 : // a번부터 b번 인덱스 까지 c간격으로
                int idx = Math.round((b - a) / 2) + 1;
                
                answer = new int[idx];
                for (int i=a; i<b+1; i+=c) {
                    answer[k++] = num_list[i];
                }
                break;
            default :
        }
        return answer;
    }
}
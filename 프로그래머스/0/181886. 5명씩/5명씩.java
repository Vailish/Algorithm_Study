class Solution {
    public String[] solution(String[] names) {
        int size = names.length%5==0 ? names.length/5 : names.length/5+1;
        String[] answer = new String[size];
        for (int i=0; i<size; i++) {
            answer[i] = names[5*i];
        }
        return answer;
    }
}
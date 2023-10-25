class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
//         "aya", "ye", "woo", "ma"를 확인해보고
//         같은 녀석이 있으면 
        for (String word : babbling) {
            String tmpWord = "";
            String exWord = "";
            for (int i=0; i<word.length(); i++) {
                tmpWord += String.valueOf(word.charAt(i));
                
                if (tmpWord.length() == 2) {
                    if (tmpWord.equals("ye") && !exWord.equals("ye")) {
                        tmpWord = "";
                        exWord = "ye";
                    } else if (tmpWord.equals("ma")&& !exWord.equals("ma")) {
                        tmpWord = "";
                        exWord = "ma";
                    }
                }
                else if(tmpWord.length() == 3) {
                    if (tmpWord.equals("aya") && !exWord.equals("aya")) {
                        tmpWord = "";
                        exWord = "aya";
                    } else if (tmpWord.equals("woo")&& !exWord.equals("woo")) {
                        tmpWord = "";
                        exWord = "woo";
                    } else {break;}
                }
                
                }
                // 확인
                if (tmpWord.equals("")) {
                    answer += 1;
            }
        }
        return answer;
    }
}
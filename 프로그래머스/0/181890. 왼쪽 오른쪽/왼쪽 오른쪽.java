import java.util.Arrays;

class Solution {
    public String[] solution(String[] str_list) {
        String state = "";
        int idx = -1;
        for (int i=0; i<str_list.length; i++) {
            if (str_list[i].equals("l")) {
                idx = i;
                state = "l";
                break;
            } else if (str_list[i].equals("r")) {
                idx = i;
                state = "r";
                break;
            }
        }
        switch (state) {
            case "l": return Arrays.copyOfRange(str_list, 0, idx);
            case "r": return Arrays.copyOfRange(str_list, idx+1, str_list.length);
            default: return new String[0];
        }
    }
}
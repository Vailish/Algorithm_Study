class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        StringBuilder result = new StringBuilder();
        for (int i=0; i<my_strings.length; i++) {
            result.append(my_strings[i].substring(parts[i][0], parts[i][1]+1));
        }
        return result.toString();
    }
}
class Solution {
    public boolean solution(boolean x1, boolean x2, boolean x3, boolean x4) {
        return caculate(0, caculate(1, x1, x2), caculate(1, x3, x4));
    }
    // V 둘 중 하나라도 True 1
    // ㅅ 둘 다 True 0
    boolean caculate(int method, boolean x, boolean y) {
        boolean result = false;
        if (method==1) {
            if (x==true || y==true) result = true;
        } else {
            if (x==true && y==true) result = true;
        }
        return result;
    }
}
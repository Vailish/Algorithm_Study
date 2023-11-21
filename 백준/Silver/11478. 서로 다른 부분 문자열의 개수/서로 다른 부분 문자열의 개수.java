import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String st = sc.next();
        HashSet<String> stringSet = new HashSet<>();
        for (int i=0; i<=st.length(); i++) {
            for (int j=i; j<=st.length(); j++) {
                stringSet.add(st.substring(i,j));
            }
        }
        System.out.println(stringSet.size()-1);
    }
}

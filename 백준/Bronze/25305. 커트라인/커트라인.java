import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int o = sc.nextInt();

        List<Integer> nums = new ArrayList<>();
        int idx = 0;
        while (idx<n) {
            nums.add(sc.nextInt());
            idx++;
        }
        nums.sort(Comparator.reverseOrder());
        System.out.println(nums.get(o-1));
    }
}

import java.util.*;

public class LeastCommonMultiple {

    private static long lcm_fast(int a, int b) {

        return ((long) a * b) / gcd_euclid(a, b);
    }

    private static int gcd_euclid(int a, int b) {

        if (b == 0)
            return a;

        return gcd_euclid(b, a % b);
    }

    public static void main(String args[]) {

        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        scanner.close();

        System.out.println(lcm_fast(a, b));
    }
}
import java.util.*;

public class FibonacciHuge {

    private static long getFibonacciHugeFast(long n, long m) {

        long remainder = n % get_pisano_period_number(m);

        long a = 0;
        long b = 1;

        long result = remainder;
        // System.out.println(remainder);

        for (int i = 1; i < remainder; i++) {
            result = (a + b) % m;
            a = b;
            b = result;
        }

        return result % m;
    }

    private static long get_pisano_period_number(long m) {

        long a = 0, b = 1, c = a + b;
        for (int i = 0; i < m * m; i++) {
            c = (a + b) % m;
            a = b;
            b = c;
            if (a == 0 && b == 1)
                return i + 1;
        }

        return -1;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long m = scanner.nextLong();
        scanner.close();

        System.out.println(getFibonacciHugeFast(n, m));
    }
}
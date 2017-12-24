import java.util.*;

public class FibonacciLastDigit {

    private static int getFibonacciLastDigitFast(int n) {

        if (n <= 1)
            return n;

        int previous = 0;
        int current = 1;

        for (int i = 0; i < n - 1; ++i) {
            int tmp_previous = previous;
            previous = current;
            current = (tmp_previous + current) % 10;
        }

        return current % 10;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();

        int c = getFibonacciLastDigitFast(n);
        System.out.println(c);
    }
}
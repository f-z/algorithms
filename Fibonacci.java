import java.math.BigInteger;
import java.util.Scanner;

public class Fibonacci {

    private static BigInteger calc_fib(int n) {

        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;

        for (int bit = Integer.highestOneBit(n); bit != 0; bit >>>= 1) {

            BigInteger d = multiply(a, b.shiftLeft(1).subtract(a));
            BigInteger e = multiply(a, a).add(multiply(b, b));
            a = d;
            b = e;

            if ((n & bit) != 0) {
                BigInteger c = a.add(b);
                a = b;
                b = c;
            }
        }
        return a;
    }

    public static void main(String args[]) {

        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        in.close();

        System.out.println(calc_fib(n));
    }

    private static BigInteger multiply(BigInteger x, BigInteger y) {

        return x.multiply(y);
    }
}
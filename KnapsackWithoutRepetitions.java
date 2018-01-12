import java.util.*;

public class Knapsack {
    static int optimalWeight(int W, int[] w) {
        int i, j;
        int results[][] = new int[w.length + 1][W + 1];

        // building values table in bottom-up manner
        for (i = 0; i <= w.length; i++) {
            for (j = 0; j <= W; j++) {
                if (i == 0 || j == 0)
                    results[i][j] = 0;
                else if (w[i - 1] <= j)
                    // weights are equal to values since all bars are the same
                    // (gold)
                    results[i][j] = max(w[i - 1] + results[i - 1][j - w[i - 1]], results[i - 1][j]);
                else
                    results[i][j] = results[i - 1][j];
            }
        }

        return results[w.length][W];
    }

    static int naiveWeight(int W, int[] w) {
        int result = 0;
        for (int i = 0; i < w.length; i++) {
            if (result + w[i] <= W) {
                result += w[i];
            }
        }
        return result;
    }

    // utility function returning the maximum of two integers
    static int max(int a, int b) {
        return (a > b) ? a : b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int W, n;
        W = scanner.nextInt();
        n = scanner.nextInt();

        int[] w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = scanner.nextInt();
        }
        scanner.close();

        System.out.println(optimalWeight(W, w));
    }
}

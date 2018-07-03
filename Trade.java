class Trade {
    static int maximumProfit(int[] price, int n, int k) {
        int[][] profit = new int[k + 1][n + 1];

        for (int i = 0; i <= k; i++)
            profit[i][0] = 0;

        for (int j = 0; j <= n; j++)
            profit[0][j] = 0;

        for (int i = 1; i <= k; i++) {
            for (int j = 1; j < n; j++) {
                int maximum_so_far = 0;

                for (int m = 0; m < j; m++)
                    maximum_so_far = Math.max(maximum_so_far, price[j] - price[m] + profit[i - 1][m]);

                profit[i][j] = Math.max(profit[i][j - 1], maximum_so_far);
            }
        }

        return profit[k][n - 1];
    }

    public static void main(String[] args) {
        int k = 4;
        int[] price = { 1, 12, 3, 5 };
        int n = price.length;
        System.out.println("The maximum profit is: " + maximumProfit(price, n, k));
    }
}

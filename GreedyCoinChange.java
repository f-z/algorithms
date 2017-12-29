import java.util.Scanner;

public class GreedyCoinChange {
    private static int getChange(int m) {

        int numberOfCoins = 0;
        int remainder = m;

        for (int unit = 10; unit >= 1; unit--) {
            if (unit == 10 || unit == 5 || unit == 1) {
                numberOfCoins += remainder / unit;
                remainder %= unit;
            }
        }
        
        return numberOfCoins;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        scanner.close();

        System.out.println(getChange(m));
    }
}

import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Arrays;
import java.util.Scanner;

public class GreedyFractionalKnapsack {

    class Item implements Comparable<Item> {
        int value, weight;

        Item(int value, int weight) {
            this.value = value;
            this.weight = weight;
        }

        // comparison function to sort input arrays according to value/weight
        // ratio
        @Override
        public int compareTo(Item o) {
            double r1 = (double) this.value / this.weight;
            double r2 = (double) o.value / o.weight;
            return Double.compare(r2, r1);
        }
    }

    private static double getOptimalValue(int capacity, Item[] items) {
        Arrays.sort(items);

        double value = 0;
        int index = 0;

        while (capacity > 0 && index < items.length) {
            if (items[index].weight <= capacity) {
                capacity -= items[index].weight;
                value += items[index].value;
                index++;
            } else {
                value += capacity * ((double) items[index].value / items[index].weight);
                capacity = 0;
            }
        }

        return value;
    }

    public static void main(String args[]) {

        GreedyFractionalKnapsack sack = new GreedyFractionalKnapsack();

        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            items[i] = sack.new Item(scanner.nextInt(), scanner.nextInt());
        }
        scanner.close();

        DecimalFormat df = new DecimalFormat("#.###");
        df.setRoundingMode(RoundingMode.CEILING);
        System.out.println(df.format(getOptimalValue(capacity, items)));
    }
}

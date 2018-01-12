import java.util.*;

public class PrimitiveCalculator {
    private static List<Integer> greedy_optimal_sequence(int n) {
        List<Integer> sequence = new ArrayList<Integer>();

        while (n >= 1) {
            sequence.add(n);
            if (n % 3 == 0) {
                n /= 3;
            } else if (n % 2 == 0) {
                n /= 2;
            } else {
                n -= 1;
            }
        }

        Collections.reverse(sequence);
        return sequence;
    }

    private static ArrayList<Integer> dynamic_optimal_sequence(int n) {
        int[] minNumberSteps = new int[n + 1];
        int[] predecessor = new int[n + 1];
        
        for (int i = 2; i <= n; i++) {
            minNumberSteps[i] = minNumberSteps[i - 1] + 1;
            predecessor[i] = i - 1;
            if (i % 3 == 0) {
                if (minNumberSteps[i / 3] < minNumberSteps[i]) {
                    minNumberSteps[i] = minNumberSteps[i / 3] + 1;
                    predecessor[i] = i / 3;
                }
            }
            if (i % 2 == 0) {
                if (minNumberSteps[i / 2] < minNumberSteps[i]) {
                    minNumberSteps[i] = minNumberSteps[i / 2] + 1;
                    predecessor[i] = i / 2;
                }
            }
        }

        ArrayList<Integer> sequence = new ArrayList<Integer>();

        for (int i = n; i != 0; i = predecessor[i]) {
            sequence.add(i);
        }
        
        Collections.reverse(sequence);
        return sequence;
    }

    public static void main(String[] args) {
        // test with 96234 to see the difference between the greedy non-optimal solution and the dynamic one
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();

        List<Integer> greedySequence = greedy_optimal_sequence(n);
        
        System.out.println("Greedy sequence minimum number of steps: " + (greedySequence.size() - 1));

        System.out.println("Greedy sequence path:");
        for (int x = 0; x < greedySequence.size(); x++) {
            System.out.print(greedySequence.get(x) + " ");
        }
        
        ArrayList<Integer> dynamicSequence = dynamic_optimal_sequence(n);

        System.out.println("\nDynamic sequence minimum number of steps: " + (dynamicSequence.size() - 1));
        
        System.out.println("Dynamic sequence path:");
        for (int x = 0; x < dynamicSequence.size(); x++) {
            System.out.print(dynamicSequence.get(x) + " ");
        }
    }
}
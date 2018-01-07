import java.util.*;
import java.io.*;

public class MajorityElement {
    private static int getMajorityElement(int[] a, int left, int right) {
        if (left > right) {
            return -1;
        }
        if (left == right) {
            return a[left];
        }

        int middle = left + (right - left) / 2;

        int leftElement = getMajorityElement(a, left, middle);
        int rightElement = getMajorityElement(a, middle + 1, right);

        if (leftElement == -1 && rightElement != -1) {
            int num = count(a, left, right, rightElement);
            if (num > (right - left + 1) / 2)
                return rightElement;
        } else if (rightElement == -1 && leftElement != -1) {
            int num = count(a, left, right, leftElement);

            if (num > (right - left + 1) / 2) {
                return leftElement;
            }
        } else if (leftElement != -1 && rightElement != -1) {
            int leftNum = count(a, left, right, leftElement);
            int rightNum = count(a, left, right, rightElement);

            if (leftNum > (right - left + 1) / 2) {
                return leftElement;
            } else if (rightNum > (right - left + 1) / 2) {
                return rightElement;
            }
        }

        return -1;
    }

    private static int count(int[] a, int left, int right, int x) {
        int count = 0;

        for (int i = left; i <= right; i++) {
            if (a[i] == x)
                count++;
        }

        return count;
    }

    public static void main(String[] args) {
        FastScanner scanner = new FastScanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        if (getMajorityElement(a, 0, a.length - 1) != -1) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}

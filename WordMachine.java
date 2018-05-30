import java.util.*;

public class WordMachine {

    public static int solution(String S) {
        // write your code in Java SE 8
        Stack<Integer> st = new Stack<Integer>();
        String[] split = S.split("\\s+");

        int result = -1;

        try {
            for (int i = 0; i < split.length; i++) {
                if (isInteger(split[i], 10)) {
                    st.push(Integer.parseInt(split[i]));
                } else {
                    int value1 = -1;
                    int value2 = -1;

                    switch (split[i]) {
                    case "POP":
                        st.pop();
                        break;
                    case "DUP":
                        value1 = (int) st.peek();
                        st.push(value1);
                        break;
                    case "+":
                        value1 = Integer.valueOf(st.pop());
                        value2 = Integer.valueOf(st.pop());
                        st.push(value1 + value2);
                        break;
                    case "-":
                        value1 = Integer.valueOf(st.pop());
                        value2 = Integer.valueOf(st.pop());
                        st.push(value1 - value2);
                        break;
                    }
                }
            }

            result = Integer.valueOf(st.peek());
        } catch (Exception e) {
            return result;
        }

        return result;
    }

    public static boolean isInteger(String s, int radix) {
        Scanner sc = new Scanner(s.trim());
        if (!sc.hasNextInt(radix))
            return false;
        sc.nextInt(radix);
        return !sc.hasNext();
    }

    public static void main(String[] args) {

        String s = "13 DUP 4 POP 5 DUP + DUP + -";

        System.out.println(solution(s));
    }
}
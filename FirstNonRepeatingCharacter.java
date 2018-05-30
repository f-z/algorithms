import java.util.*;

public class FirstNonRepeatingCharacter {
	public char findNonRepeating(String s) {
		HashMap<Character, Integer> charCount = new HashMap<Character, Integer>();

		for (int i = 0; i < s.length(); i++) {
			char c = s.charAt(i);
			if (charCount.get(c) != null) {
				charCount.put(c, charCount.get(c) + 1);
			}
			else {
				charCount.put(c, 1);
			}
		}

		for (int i = 0; i < s.length(); i++) {
			if (charCount.get(s.charAt(i))==1) {
				return s.charAt(i);
			}
		}

		return -1;

	}
}

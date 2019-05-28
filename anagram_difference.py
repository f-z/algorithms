# !/bin/python3


def count_modifications(string_1, string_2):
    # Initial check
    if len(string_1) != len(string_2):
        return -1

    # Initialization of mod count and alphabetical character count
    count = 0
    character_count = [0] * 26
    for i in range(26):
        character_count[i] = 0

    # Going through the first string and counting occurrences of each character
    for i in range(len(string_1)):
        character_count[ord(string_1[i]) - ord('a')] += 1

    # Going through the second string and deducting occurences of each character
    for i in range(len(string_2)):
        character_count[ord(string_2[i]) - ord('a')] -= 1
        # If character does not exist in first string
        if character_count[ord(string_2[i]) - ord('a')] < 0:
            # One more modification needs to be done
            count += 1

    # After having gone through both strings, return total modification count
    return count

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Different lengths cannot be anagrams
        if len(s) != len(t):
            return False

        count = [0] * 26  # 26 lowercase English letters

        # Add frequency of characters from s
        for ch in s:
            count[ord(ch) - ord('a')] += 1          #increase kr rhe 

        # Subtract frequency of characters from t
        for ch in t:
            count[ord(ch) - ord('a')] -= 1          #decrease kr rhe 

        # Check whether all frequencies became 0
        for x in count:
            if x != 0:
                return False

        return True
class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            next_str = ""
            i = 0

            while i < len(current):
                count = 0
                ch = current[i]

                while i < len(current) and current[i] == ch:
                    count += 1
                    i += 1

                next_str += str(count) + ch

            current = next_str

        return current
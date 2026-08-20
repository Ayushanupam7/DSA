class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n):
            total = 0
            while n:
                n, digit = divmod(n, 10)
                total += digit * digit
            return total

        slow = n
        fast = next_num(n)

        while fast != 1 and slow != fast:
            slow = next_num(slow)
            fast = next_num(next_num(fast))

        return fast == 1
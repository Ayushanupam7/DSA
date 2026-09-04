class Solution:
    def addDigits(self, num: int) -> int:
        # Base case: if single digit, stop recursing
        if num < 10:
            return num
        
        # Recursive step: calculate new sum and call function again
        new_sum = 0
        while num > 0:  # You can keep this inner loop for math, or use recursion there too
            new_sum += num % 10
            num //= 10
            
        return self.addDigits(new_sum)
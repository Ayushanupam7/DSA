class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:            # keep going while 2+ digits
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10   # grab last digit
                num //= 10              # remove last digit
            num = digit_sum
        return num
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid      # mid is a valid candidate
                left = mid + 1 # try for something bigger
            else:
                right = mid - 1
        return ans
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0:
            return 0

        left = 1
        right = x
        ans = 0

        while left <= right:

            # Middle number check karenge
            mid = (left + right) // 2

            # Agar mid ka square x se chhota ya equal hai,
            # to mid ek possible answer hai
            if mid * mid <= x:
                ans = mid

                # Answer mil gaya, ab isse bada number try karo
                left = mid + 1

            else:
                # mid bahut bada hai,
                # isliye right side ko chhota karo
                right = mid - 1

        # Last valid answer return karo
        return ans
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev2 = 1  # Represents ways to reach (n-2)   #if i check for 3; 3-2=1,4-2=2
        prev1 = 2  # Represents ways to reach (n-1)    #if i check for 3; 3-1=2,4-1=3
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1


#Two parts
#like first is check if number is less than 2 or equal to 2 then return same number 
#
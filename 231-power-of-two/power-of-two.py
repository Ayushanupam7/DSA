class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

            if n > 0 and n & (n - 1) == 0:   
                return True 
            return False 


# There are two different operators here:
#
# 1. "and" → Logical AND
#    Used to combine conditions.
#    True and True   → True
#    True and False  → False
#
# 2. "&" → Bitwise AND
#    Does NOT convert integer to binary.
#    Performs AND operation on the bits.
#
# 🔥 Power of Two Logic:
#
# Power of 2 → exactly ONE '1' bit
#
# Example:
#   8     → 1000
#   8 - 1 → 0111
#
#     1000
#   & 0111
#   ------
#     0000  → Power of 2 ✅
#
# Non-power:
#   6     → 0110
#   6 - 1 → 0101
#
#     0110
#   & 0101
#   ------
#     0100  → Not power of 2 ❌
#
# Formula:
#   n > 0 and n & (n - 1) == 0
#
# "and" → checks conditions
# "&"   → checks bits
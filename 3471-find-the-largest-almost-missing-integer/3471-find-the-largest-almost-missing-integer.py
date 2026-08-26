from collections import defaultdict
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        n = len(nums)
        
        # 1. Har size-k subarray ke unique elements ka count badhao
        for i in range(n - k + 1):
            subarray = nums[i : i + k]
            for num in set(subarray):
                count[num] += 1
                
        # 2. Jo number exactly 1 subarray me aaya, unme se sabse bada number dhoondho
        ans = -1
        for num, freq in count.items():
            if freq == 1:
                ans = max(ans, num)
                
        return ans
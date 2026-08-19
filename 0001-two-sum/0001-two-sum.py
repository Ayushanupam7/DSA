class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen:
                return [seen[needed], i]

            seen[nums[i]] = i
            
  #    for i in range (len(nums)):
    #     for j in range(i + 1,len(nums)):
    #         total= nums[i]+nums[j]
    #         if total == target:
    #             return[i,j]     // Brute Force Approach
            

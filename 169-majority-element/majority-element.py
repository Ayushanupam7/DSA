class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}  # har number ki frequency store karega

        for i in range(len(nums)):
            # check kar rahe hain ki current number dictionary me hai ya nahi
            if nums[i] in count:
                count[nums[i]] += 1  # already hai, to count badhao
            else:
                count[nums[i]] = 1   # pehli baar mila, count 1

            # majority element n/2 se zyada baar hona chahiye..
            if count[nums[i]] > len(nums) / 2:
                return nums[i]
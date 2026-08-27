class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        frequency = [0] * 101

        # Count frequency of every number
        for num in nums:
            frequency[num] += 1

        # Find maximum frequency
        max_frequency = max(frequency)

        # Add frequencies of elements having maximum frequency
        answer = 0

        for freq in frequency:
            if freq == max_frequency:
                answer += freq

        return answer
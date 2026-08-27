class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        freq1 = [0] * 1001
        freq2 = [0] * 1001

        # Count frequency in nums1
        for i in nums1:
            freq1[i] += 1

        # Count frequency in nums2
        for j in nums2:
            freq2[j] += 1

        # Build the answer
        result = []

        for i in range(1001):
            common = min(freq1[i], freq2[i])

            for _ in range(common):
                result.append(i)

        return result
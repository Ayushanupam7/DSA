class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        low = 0
        mid = 0
        high = len(nums) - 1
        
        
        while mid <= high:
            if nums[mid] == 0:
               
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 apni jagah par sahi hai, bas aage badho
                mid += 1
            else:  # nums[mid] == 2
                # 2 ko right side (high position) par bhejo
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

                # Loop jab tak mid high ko cross na kar de
                 # 0 ko left side (low position) par bhejo
                # Note: mid ko yahan increment NAHI kar rahe,
                # kyunki naye element ko check karna baaki hai
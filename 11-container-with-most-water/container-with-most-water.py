class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Start from the first line
        left = 0

        # Start from the last line
        right = len(height) - 1

        # Store the maximum area found
        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])

            # Formula:
            # Area = Width × Height
            area = width * current_height

            # Keep the largest area found so far
            max_area = max(max_area, area)

            # -----------------------------------------
            # IMPORTANT:
            #
            # Move the pointer having SMALLER height.
            #
            # Why?
            # The smaller line is limiting the water.
            #
            # If left is smaller:
            #
            # left  → move right
            #
            # If right is smaller:
            #
            # right → move left
            # -----------------------------------------

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return the largest container area
        return max_area


        # -----------------------------------------
            # VISUAL:
            #
            # left                   right
            #  ↓                       ↓
            # [1, 8, 6, 2, 5, 4, 8, 3, 7]
            #
            # These two lines make the container
            # -----------------------------------------

            # Distance between the two lines
            # This is the WIDTH of the container
            # The shorter line decides how much water
            # the container can hold.
            #
            # Example:
            # left height  = 8
            # right height = 7
            #
            # Water height = 7
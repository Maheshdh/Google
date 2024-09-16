class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height)-1
        while left < right:
            left_height = height[left]
            right_height = height[right]
            max_water = max(max_water, min(left_height,right_height) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water

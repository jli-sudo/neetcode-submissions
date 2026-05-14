class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0

        for i in range(len(height)):
            max_left = max(height[:i + 1])
            max_right = max(height[i:])
            water = min(max_left, max_right) - height[i]
            total_water += water
        
        return total_water
            

        

class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(len(height)):
            leftMax = 0
            rightMax = 0
            for j in range(0,i+1):
                leftMax = max(leftMax,height[j])
            for k in range(i,len(height)):
                rightMax = max(rightMax,height[k])
            water += min(leftMax,rightMax)-height[i]
        return water
        
                



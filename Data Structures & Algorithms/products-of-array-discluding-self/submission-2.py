class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [math.prod(nums[:i])*math.prod(nums[i+1:])for i in range(len(nums))]
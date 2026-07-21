class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set= set(nums)
        res = 0
        for num in nums:
            if num-1 not in num_set:
                length = 1
                while num+1 in num_set:
                    length+=1
                    num+=1
                res=  max(res,length)
        return res

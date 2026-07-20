class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_common = counts.most_common(k)
        return [num for num, freq in most_common]


        
        
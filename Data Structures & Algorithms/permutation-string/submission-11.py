class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i:i+len(s1)]
            if Counter(sub) == count1:
                return True
        return False
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cnt = 0 
        a=[]
        for i in nums:
            cnt = i+cnt
            a.append(cnt)
        return a
        
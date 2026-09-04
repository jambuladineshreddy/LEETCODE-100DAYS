class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        sf=[0]*n
        sf[n-1]=nums[-1]
        for s in range(n-2,-1,-1):
            sf[s]=min(sf[s+1],nums[s])
        maxfar=nums[0]
        small=0
        mini=0
        for i in range(len(nums)):
            if nums[i]>maxfar:
                maxfar=nums[i]
            if maxfar-sf[i]<=k:
                return i
        
        return -1
            

        
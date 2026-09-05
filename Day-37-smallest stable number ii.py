class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        st=[0]*n
        st[n-1]=nums[n-1]
        for s in range(n-2,-1,-1):
            st[s]=min(nums[s],st[s+1])
        mfn=0

        for i in range(n):
            if mfn>nums[i]:
                mfn=nums[i]
            if mfn-st[i]<=k:
                return i
        return -1
            

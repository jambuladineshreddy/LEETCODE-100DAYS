class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        s=0
        diff=0
        hm={}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
            while hm[nums[i]]>k:
                hm[nums[s]] -= 1
                s+=1
            cdiff=i-s+1
            diff=max(diff,cdiff)
        return diff


        
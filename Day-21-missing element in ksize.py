class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        hm={}
        for i in range(n):
            hm[nums[i]] = hm.get(nums[i], 0) + 1 
        if k==1:
            ans=-1
            for num in nums:
                if hm[num]==1:
                    ans=max(ans,num)
            return ans           
        if k==n:
            return max(nums)
        if hm[nums[0]]>1 and hm[nums[n-1]]>1:
            return -1
        elif hm[nums[0]]>1 :
            return nums[n-1]
        elif hm[nums[n-1]]>1:
            return nums[0]
        else:
            return max(nums[0],nums[n-1])
        
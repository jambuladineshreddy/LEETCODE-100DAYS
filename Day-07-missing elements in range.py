class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=nums[0]
        h=nums[0]
       
        for num in nums:
            if num>h:
                h=num
            elif num<l:
                l=num
        s=set(nums)
        ans=[]
        for i in range(l,h):
            if i not in s:
                ans.append(i)
            
        return ans

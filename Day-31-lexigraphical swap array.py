class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups=[]
        map={}
        for n in sorted(nums):
            if not groups or (n-groups[-1][-1])>limit:
                groups.append(deque())
            groups[-1].append(n)
            map[n]=len(groups)-1
        res=[]
        for n in nums:
            j=map[n]
            res.append(groups[j].popleft())
        return res
        
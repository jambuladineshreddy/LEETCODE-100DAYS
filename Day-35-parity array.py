class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        # Find the minimum element in the array
        mn = min(nums1)
        
        # If the minimum element is odd, we can make all elements odd
        if mn % 2 == 1:
            return True
        else:
            # If the minimum is even, all elements MUST already be even
            for num in nums1:
                if num % 2 == 1:
                    return False # Found an odd number, impossible to convert
                    
        return True
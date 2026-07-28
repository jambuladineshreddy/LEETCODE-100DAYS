from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)

        left = []
        middle = ""
        for ch in sorted(freq.keys()):
            left.append(ch * (freq[ch] // 2))
            if freq[ch] % 2 == 1:
                middle = ch
        left_half = "".join(left)

        right_half = left_half[::-1]
        return left_half + middle + right_half
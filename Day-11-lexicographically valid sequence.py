class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = position in word1 from which
        # word2[j:] can be matched
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        # Exact subsequence is impossible
        # even after allowing one mismatch
        if last[0] == -1:
            return []

        ans = []
        used_mismatch = False
        j = 0

        for i in range(n):
            if j == m:
                break

            # Characters already match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif not used_mismatch:
                # If this is the last character,
                # no suffix needs to be checked.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    used_mismatch = True
                    j += 1

        if j == m:
            return ans

        return []
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        answer = 0

        for h in range(n + 1):
            count = 0

            for citation in citations:
                if citation >= h:
                    count += 1

            if count >= h:
                answer = h

        return answer
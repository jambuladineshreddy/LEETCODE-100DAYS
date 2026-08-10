class Solution:
    def winnerSquareGame(self, n):
        memo = {}

        def game(n, isAlice):
            if n == 0:
                return not isAlice

            if (n, isAlice) in memo:
                return memo[(n, isAlice)]

            i = 1

            while i * i <= n:
                if isAlice:
                    if game(n - i * i, False):
                        memo[(n, isAlice)] = True
                        return True
                else:
                    if not game(n - i * i, True):
                        memo[(n, isAlice)] = False
                        return False

                i += 1

            memo[(n, isAlice)] = not isAlice
            return not isAlice

        return game(n, True)
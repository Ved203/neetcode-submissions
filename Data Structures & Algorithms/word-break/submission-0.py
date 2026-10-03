class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = {}

        def dfs(i: int) -> bool:
            # Base case: Reached the end of the string successfully
            if i == len(s):
                return True
            
            # Return cached result if we've already evaluated this index
            if i in memo:
                return memo[i]

            # Try matching every word from wordDict starting at index i
            for word in wordDict:
                w_len = len(word)
                if i + w_len <= len(s) and s[i : i + w_len] == word:
                    if dfs(i + w_len):
                        memo[i] = True
                        return True

            # If no word leads to a valid breakdown, memoize and return False
            memo[i] = False
            return False

        return dfs(0)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] will be True if s[i:] matches p[j:]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: empty string matches empty pattern
        dp[len(s)][len(p)] = True
        
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                # Check if current characters match
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                
                # If next character in pattern is '*'
                if j + 1 < len(p) and p[j + 1] == '*':
                    # Two choices:
                    # 1. Skip current character and '*' (0 occurrences)
                    # 2. Use '*' if first_match, moving forward in string `s`
                    dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
                else:
                    # Standard character match
                    dp[i][j] = first_match and dp[i + 1][j + 1]
                    
        return dp[0][0]
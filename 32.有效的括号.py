class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)        
        dp = [0 for i in range(n)]  # 状态参数dp[i]:表示以s[i]结尾的最长有效括号的长度
        result = 0
        for i in range(1, len(s)):  # 从s的第二个字母开始遍历；避免越界；同时第一项无需比较必定为0
            if s[i] == ')':     #   s[i] == '('  那么dp[i] =0;所以只用从s[i] == ')'开始
                if s[i-1] == '(':
                    dp[i] = ((dp[i-2] + 2) if i >= 2 else 2)
                elif i-1-dp[i-1] >= 0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + (dp[i-2-dp[i-1]] if i-2-dp[i-1]>=0 else 0) + 2     # s[i-1] = s[i] = ')'
            result = max(result,dp[i])
        return result

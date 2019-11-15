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


"""解法二： 用栈来解决、进栈的元素是字符串下标索引
		
思路如下：1. 初始化时先把-1进栈	# 防止栈空，弹出失败		
		  2. 每遇到一个左括号把该括号的下标入栈
		  3. 要是遇到右括号：1. 先弹出栈顶元素
							 2. 判断是否为空：如果为空，填入当前元素下标
											  否则 maxlength = max(maxlength, i - stack[-1])
			难点：遍历中途栈为空了怎么办：特别时栈空后紧跟着一个'('括号，如果这时入栈的是当前括号下标i，常规思路那么就有问题。
					解决办法就是：假设刚开始左边就是有很多个')',我们只用记录紧邻第一个左括号的右括号下标当flag即可。
								  所以栈底弄一个标记flag = -1;只要栈空后不是左括号(前后连接不上)，那么就可以重新计数了，弹出flag = -1 装入新的flag = i:即当前右括号下标
								  如果栈空后是左括号，那好，我继续入栈。那么当后面有左括号时，弹出该元素，跟其相减的时flag = -1 正好续上了"""
	
def longestValidParentheses2(s: str) -> int:
	stack = []	# 记录进栈的左括号下标
	maxlength = 0
	stack.append(-1)
	for i in range(len(s)):
		if s[i] == '(':
			stack.append(i)
		else:
			stack.pop()
			if len(stack) == 0:
				stack.append(i)
			else:
				maxlength = max(maxlength, i - stack[-1])
	return maxlength
			


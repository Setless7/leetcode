class Solution:
	def lengthOfLongestSubstring(self, s) -> int:
		maxSubstringLength = 0
		head = 0
		tail = 0
		for tail in range(len(s)):
			if  s[tail] in s[head:tail]:
				if tail - head  > maxSubstringLength:
					maxSubstringLength = tail - head 
				head += s[head:tail].index(s[tail])+1
		if tail - head + 1 > maxSubstringLength and len(s) != 0:
			maxSubstringLength = tail - head + 1 
		return maxSubstringLength


s = ''
a = Solution()
max = a.lengthOfLongestSubstring(s)
print(max)
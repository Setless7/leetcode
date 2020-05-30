class Solution:
	def reverse(self, x) -> int:
		intReverse = 0
		flag= -1 if x<0 else 1
		x = flag * x
		while x != 0:
			intReverse = intReverse * 10 + x%10
			x //= 10
		if intReverse * flag < -2147483647 or intReverse * flag>2147483647:
			return 0
		return intReverse * flag

s = -123
a = Solution()
t = a.reverse(s)
print(t)
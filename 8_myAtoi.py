class Solution:
	def myAtoi(self, str) -> int:
		hashdict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
		flag = 1
		result = 0
		str = str.strip()
		if str == '':
			return 0
		if str[0] == '-':
			flag = -1
			str = str[1:]
		elif str[0] == '+':
			str = str[1:]
		for i in str:
			if hashdict.__contains__(i):
				result = result*10+hashdict[i]
			if not hashdict.__contains__(i):
				break
		result *= flag
		if result<-2147483648 :
			return -2147483648
		elif result>2147483647:
		   return 2147483647
		return result
s = "  -4193 with words"
a = Solution()
t = a.myAtoi(s)
print(t)


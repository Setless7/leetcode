class Solution:
	def longestPalindrome(self, s) -> str:
		if len(s) <= 1:
			return s
		indexListDouble,indexListSingle =  self.findShortestPalindrome(s)
		maxSingle = 0
		maxDouble = 0
		if indexListDouble or indexListSingle:
			if indexListDouble:
				maxDouble = 2
				maxDoubleStr = s[indexListDouble[0]-1:indexListDouble[0] + 1]
			if indexListSingle:
				maxSingle = 3
				maxSingleStr = s[indexListSingle[0]-1:indexListSingle[0] + 2]
		else:
			return s[0]
		
		
		for i in indexListDouble:
			breakFlage = 0
			j = 0
			for j in range(1,i):
					if i + j < len(s) and s[i + j] != s[i - j -1] :
						breakFlage = 1
						if 2 * (j) > maxDouble:
							maxDouble =  2 * (j)
							maxDoubleStr = s[i - j : i + j ]
						break
					elif i + j >= len(s) :#2 * j  > maxDouble:
						breakFlage = 1
						if 2 * (j) > maxDouble:
							maxDouble =  2 * (j)
							maxDoubleStr = s[i - j : i + j ]
						break
			if breakFlage != 1 and j != 0:
				maxDouble = 2 * i
				maxDoubleStr = s[0:2*i]
		
		for i in indexListSingle:
			j = 0
			breakFlage = 0
			for j in range(1,i+1 ):
					if i+j<len(s) and s[i  + j] != s[i - j ] :
						breakFlage = 1
						if 2 * (j-1) + 1 > maxSingle:
							maxSingle = 2 * (j-1) + 1
							maxSingleStr = s[i - j + 1: i + j ]
						break
					elif i+j>=len(s):
						breakFlage = 1
						if 2*(j-1) + 1>maxSingle:
							maxSingle = 2*(j-1) + 1
							maxSingleStr = s[i - j +1: i + j + 1]
						break
			if breakFlage == 0 and j != 0:
				maxSingle = 2 * i + 1
				maxSingleStr = s[0: 2 * i + 1]
		if maxDouble > maxSingle:
			return maxDoubleStr
		else :
			return maxSingleStr
	def findShortestPalindrome(self,s)->list:
		indexListDouble = []
		indexListSingle = []
		i = 0
		for i in range(1,len(s)-1):
			if s[i-1] == s[i]:
				indexListDouble.append(i)
			if s[i-1] == s[i + 1]:
				indexListSingle.append(i)
		if s[i+1] == s[i]:
			indexListDouble.append(i+1)
		return indexListDouble,indexListSingle


s = 'babad'
a = Solution()
t = a.longestPalindrome(s)
print(t)
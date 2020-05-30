class Solution:
	def convert(self, s, numRows) -> str:
		if numRows == 1:
			return s
		listGaps = []
		strCovert = ''
		for i in range(numRows):
			if i ==0 or i == numRows -1:
				listGaps =[(numRows - 1)*2,(numRows - 1)*2]
			else :
				listGaps =[(numRows -i- 1)*2,2 * i ]
			nextIndex = i
			gapIndex = 0
			while nextIndex < len(s):
				strCovert += s[nextIndex]
				nextIndex += listGaps[gapIndex]
				gapIndex = 0 if gapIndex == 1 else 1	
		return strCovert
s = 'LEETCODEISHIRING'
a = Solution()
t = a.convert(s,4)
print(t)
class Solution:
	def isMatch(self, s, p) -> bool:
		sList = list(s)
		pList = list(p)
		while(pList[0] == '*'):
			pList.pop(0)
		i = 0
		while i < len(pList) - 1:
			if pList[i] == '*' and pList[i+1] == pList[i-1]:
				pList.pop(i+1)
			else:
				i+=1
		while sList:
			if not pList :
				return False
			if len(pList) == 1:
				if (sList[0] == pList[0] or pList[0] == '.'):
					sList.pop(0)
					pList.pop(0)
				else:
					return False
			elif (sList[0] == pList[0] or pList[0] == '.') and pList[1] != '*':
				sList.pop(0)
				pList.pop(0)
			elif (sList[0] == pList[0] or pList[0] == '.') and pList[1] == '*':
				sList.pop(0)
				if not sList:
					pList.pop(0)
					pList.pop(0)
			elif pList[1] == '*':
				pList.pop(0)
				pList.pop(0)
			else :
				return False
		if pList :
			return False
		else:
			return True

s = "aaa"
p = 'a*aaaaa'
a = Solution()
t = a.isMatch(s,p)
print(t)
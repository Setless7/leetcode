class Solution:
	def twoSum(self,numlist,target)->list:
		dicts = {}
		for i in range(len(numlist)):
			j_target = target -  numlist[i]
			if (j_target in dicts):
				return [dicts[j_target],i]
			dicts[numlist[i]] = i
numlist = [2,5,5,10]		
a = Solution()
target = 10
lists = a.twoSum(numlist,target)
print(lists)
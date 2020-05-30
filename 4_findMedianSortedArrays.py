class Solution:
	def findMedianSortedArrays(self, nums1, nums2) -> float:
		medium1 = int((len(nums1) + len(nums2) -1)/2) 
		medium2 = int((len(nums1) + len(nums2) -1)/2 + 0.5)
		listMix = []
		i = 0
		j = 0
		while(i + j < len(nums1) + len(nums2)):
			if(i  == len(nums1) ):
				listMix.append(nums2[j])
				j+=1
			elif(j  == len(nums2) ):
				listMix.append(nums1[i])
				i+=1
			else:
				if nums1[i] < nums2[j]:
					listMix.append(nums1[i])
					i+=1
				else:
					listMix.append(nums2[j])
					j+=1
			if(len(listMix) - 1 == medium2):
				return (listMix[medium1] + listMix[medium2])/2


nums1 = []
nums2 = [3,4]
a = Solution()
result = a.findMedianSortedArrays(nums1,nums2)
print(result)
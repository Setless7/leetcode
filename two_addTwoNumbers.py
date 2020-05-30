class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def addTwoNumbers(self, l1, l2) -> ListNode:
		list1 = 0
		list2 = 0
		ridenum = 1
		while l1.next != None:
			list1 += l1.val * ridenum
			l1 = l1.next
			ridenum *= 10
		list1 += l1.val * ridenum
		ridenum = 1
		print(type(list1))
		while l2.next != None:
			list2 += l2.val * ridenum
			l2 = l2.next
			ridenum *= 10
		list2 += l2.val * ridenum
		#num =  (int)(list1 + list2)
		list3 = list(str(list1 + list2))
		for i in range(len(list3)):
			list3[i] = int(list3[i])
		list3.reverse()
		return self.inits(list3)
	def inits(self,listOne):
		ListNodeOne = ListNode(listOne[0])
		listNodeOneNext = ListNodeOne
		for i in range(1,len(listOne)):
			listNodeOneNext.next = ListNode(listOne[i])
			listNodeOneNext = listNodeOneNext.next
		return ListNodeOne
a = Solution()
listOne = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
listTwo = [0]
ListNodeOne = a.inits(listOne)
ListNodeTwo = a.inits(listTwo)
num = a.addTwoNumbers(ListNodeOne,ListNodeTwo)
print(ListNodeOne)
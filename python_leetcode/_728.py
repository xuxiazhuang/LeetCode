A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


solution:
list1=[]
def self_dividing(left,right):
 	for i in range(left,right+1):
 		number_list=list(str(i))
 		number_list_int=[int(i)for i in number_list]
 		for j in number_list_int :
 			if 0 in number_list_int:
 				list1.append(i)
 			else:
 				if i%j!=0:
 					list1.append(i)
 	result=[t for t in range(left,right+1) if t not in list1]
 	return result
print (self_dividing(1,22))

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.



solution:
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        
        for i in A:
            if i % 2 == 1:
                odd_list.append(i)
            else:
                even_list.append(i)

        result = [None]*(len(odd_list)+len(even_list))
        result[::2] = even_list
        result[1::2] = odd_list
        return result

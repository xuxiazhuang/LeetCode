Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


soulution:
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [0] * n
    
        for i in range(n):
            left = S[i::-1].find(C)
            right = S[i::1].find(C)
            if left > 0 and right > 0:
                res[i] = min(left, right)
            if left < 0:
                res[i] = right
            if right < 0:
                res[i] = left
        return res
        
         
s='loveleetcode'
c='e'   
 # s[1::1] # oveleetcode
 # s[1::-1]# ol
 # s[::-1]#edocteelevol
 #s[::1]#loveleetcode

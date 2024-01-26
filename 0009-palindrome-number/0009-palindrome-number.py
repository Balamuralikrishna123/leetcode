class Solution:
    def isPalindrome(self, x: int) -> bool:
       numberstr = str(x)
       return numberstr == numberstr[::-1]
            


        
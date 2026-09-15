class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        org=x
        pal=0
        while x>0:
            rem=x%10
            pal=(pal*10)+rem
            x//=10
        return org==pal

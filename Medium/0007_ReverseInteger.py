class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31-1
        org=x
        x=abs(x)
        rev=0
        while x>0:
            rem=x%10
            rev=(rev*10)+rem
            x//=10
        if org<0:
            rev*=-1
        if rev>=MIN and rev<=MAX:
            return rev
        else:
            return 0

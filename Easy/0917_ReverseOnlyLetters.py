class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        test = list(s)
        i , j = 0 , len(s)-1
        while i<=j:
            if test[i].isalpha():
                if test[j].isalpha():
                    test[i] , test[j] = test[j] , test[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return ''.join(test)

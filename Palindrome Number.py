def isPalindrome(self, x: int) -> bool:
        rev=0
        x2=x
        if x<0:
            return False
        while x!=0:
            temp=x%10
            rev= rev*10 +temp
            x =x//10
        return x2==rev

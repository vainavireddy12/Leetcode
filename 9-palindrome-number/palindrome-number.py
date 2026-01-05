class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=str(x)
        b=a[::-1]
        for i in a:
            if a==b:
                return True
            else:
                return False
            

        
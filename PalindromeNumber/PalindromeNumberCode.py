class Solution(object):
    def isPalindrome(self, x):
        forward = str(x)
        
        back = forward[::-1]

        if forward == back:
            return True
        else:
            return False

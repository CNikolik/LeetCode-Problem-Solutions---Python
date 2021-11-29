# https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy
# Submission Stats:
# Runtime: 76 ms, faster than 31.30% of Python online submissions for Palindrome Number.
# Memory Usage: 13.3 MB, less than 90.67% of Python online submissions for Palindrome Number.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        
        temp = x
        reverse = 0
        
        while x > 0:
            reverse *= 10
            reverse += x % 10
            x /= 10
            
        if reverse == temp:
            return True
        
        return False

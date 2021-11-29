# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Submission Stats:
# Runtime: 32 ms, faster than 98.67% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.6 MB, less than 75.15% of Python online submissions for Longest Substring Without Repeating Characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ''
        longest = ''
        for letter in s:
            if letter not in substring:
                 substring += letter
                    
            else:
                while letter in substring:
                    substring = substring[1:]
                substring += letter
                
                
            if len(substring) > len(longest):
                longest = substring
                
        return len(longest)

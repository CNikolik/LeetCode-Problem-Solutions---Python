# https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Submission Stats: 
# Runtime: 3564 ms, faster than 26.75% of Python online submissions for Two Sum.
# Memory Usage: 14.2 MB, less than 91.55% of Python online submissions for Two Sum.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            
            for j in range(i + 1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    
                    return [i, j]  

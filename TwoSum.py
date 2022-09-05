# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num1 = 0
        num2 = 0 
        i = 0
        
        for i in range(0, len(nums)+1):
            num1 = nums[i]
            k = 10**10 #Choosing out of constraints value for the k
            j = 0
            last_element = len(nums) -1
            while j != (last_element +1):
                if j != i:
                    num2 = nums[j]
                    k = num1 + num2
                if k == target:
                    break
                j += 1
            if k == target:
                break
        
        list_indx = [i, j]
        
        return list_indx

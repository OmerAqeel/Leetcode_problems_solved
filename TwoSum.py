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

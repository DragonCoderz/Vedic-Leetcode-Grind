#Problem Description: https://leetcode.com/problems/two-sum/description/

#Solution - O(n):
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsDict = {} #Contains the following key value pair: (num, index in nums)

        #idea: iterate through nums being sure to add each element in nums to the numsDict along with its respective index. While doing so, also see if the difference of target and the current num you're at is also contained in the dictionary using dictionaries O(1) lookup property to instantly find our solution. Since a solution is guaranteed, we can keep our return statement within the for loop.

        for i, num in enumerate(nums):
            potentialSolution = target - num
            if potentialSolution in numsDict:
                return numsDict[potentialSolution], i
            else:
                numsDict[num] = i
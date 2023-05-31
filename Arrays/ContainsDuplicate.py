#Problem Description: https://leetcode.com/problems/contains-duplicate/description/

#Solution O(n):
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        visited = set() #Initialize a set to keep track of every unique element we encounter as we loop through the nums array

        for num in nums: #O(n) operation to loop through the input array once
            if num in visited: #O(1) operation to check if a value has been visited before since set values are hashed and stored in a hash table in python 
                return True
            visited.add(num) #if the element of nums we're currently looking at hasn't been seen yet, we add it to the visited set, so that it can be checked for later during out iteration process

        return False #We only reach this point if we loop through the entirety of nums and never encounter something that has been seen before more than once
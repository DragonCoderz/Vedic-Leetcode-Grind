#Problem Description: https://leetcode.com/problems/valid-anagram/description/

#Solution - O(n)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        
        CountS = {} #Stores the following key value pair: (unique character in s, respective character count)
        CountT = {} #Stores the following key value pair: (unique character in t, respective character count)

        #Idea is, if we populate these dictionaries and generate these pairs by looping through each character in s and t, if they are anagrams of one another, then they will contain identical pairs
        
        #Population process:
        for i in range(len(s)): #O(n) operation to loop through s and t concurrently once
            CountS[s[i]] = CountS.get(s[i], 0) + 1 #Key thing to note is that the get method either returns the value at the key inputted in the function, or 0 if it is not found, in O(1)
            CountT[t[i]] = CountT.get(t[i], 0) + 1

        return CountS == CountT #comparison to see whether s and t contain the same exact pairs and thus are anagrams after the population process

'''
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
'''

class Solution:
    def findBuildings(self, heights):
        a = []
        for i in range(len(heights)-1):
            for j in range(i,len(heights)):
                if heights[i] < heights[j]:
                    break
                elif heights[i] > heights[j] and j == len(heights)-1:
                    a.append(i)
        a.append(len(heights)-1)
        return a

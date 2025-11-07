
'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        x = {}
        cou_back = cou_for = 0
        cou = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                for j in range(i-1,-1,-1):
                    if seats[j] != 1:
                        cou_back += 1
                    else:
                        break
                for k in range(i+1,len(seats)):
                    if seats[k] != 1:
                        cou_for += 1
                    else:
                        break
                cou = max(cou_back, cou_for)
            if i not in x.keys():
                x[i] = cou
        y = dict(sorted(x.items(), key=lambda item:item[1], reverse=True))
        return list(y.keys())[0]

        
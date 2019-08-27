'''
252. Meeting Rooms

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''
class Solution(object):
    
    
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        #separate given intervals into starts array and ends array 
        
        starts = []
        ends = [] 
        
        
        for interval in intervals: 
            starts.append(interval[0])
            ends.append(interval[1])
        
        starts.sort()
        ends.sort()
        
        for i in range(0, len(intervals)-1): 
            if starts[i+1] < ends[i]: 
                return False 

        return True

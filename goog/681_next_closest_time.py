'''
681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''
class Solution:
    
    def nextClosestTime(self, time: str) -> str:
        
        h, m = time.split(":")
        curr = int(h) * 60 + int(m) #convert time to minutes 
        result = None
        for i in range(curr+1, curr+(24*60)+1): #simulate a clock, add minute at every iteration 
            #get military time in minutes version 
            t = i % (24*60) #1440 = 24*60 --> that is a full 360 around the clock
            
            h, m = t // 60, t % 60 #divide by 60 to get the number of hours (left most), mod by 60 to get the remaining minutes (right most)

            print("h ", h)
            print("m ", m)
            result = "%02d:%02d" % (h, m)

            if set(result) <= set(time):
                #the next time digits is always going to be smaller than equal to the give time's digit 
                print(set(result)) # 9, 1, :, 3 (19:33)
                print(set(time)) # :, 9, 1, 4, 3  (19:34)
                break
        return result

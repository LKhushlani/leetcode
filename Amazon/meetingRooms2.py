from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        1. sort by start times
        Input: intervals = [[0,30],[5,10],[15,20]]
        Output: 2
        
        2.  loop and check st if i  > end time if i-1 
        else count += 1 

        '''
        intervals.sort(key= lambda x: x[0])
        print(intervals)
        meetingRooms = []
        heapq.heappush(meetingRooms,intervals[0][1])
        print(meetingRooms)
        for i in intervals[1:]:
            print(meetingRooms,meetingRooms[0] ,i[0])
            if meetingRooms[0] <= i[0]:
                heapq.heappop(meetingRooms)
                print(meetingRooms)
            
            heapq.heappush(meetingRooms,i[1])

        print(meetingRooms)
        return len(meetingRooms)

Solution().minMeetingRooms([[9,10],[4,9],[4,17]])

'''
min heap on starting time : 
     4 , 9
  4 , 17 , 9 , 10

  9, 10 
  / 
  4,17

'''


        
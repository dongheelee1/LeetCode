'''
973. K Closest Points to Origin

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
 

Note:

1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
sort solution 
'''

'''
go through the list of points 
 calculate the euclidian distance 
 
'''
class Solution(object):
    def kClosest(self, points, K):
        import heapq
        heap = []
        for p in points:
            x, y = p[0], p[1]
            #get the euc distance 
            dist = -(x*x + y*y)
            
            #python heap is originally a min heap keeping the smallest value at the root,
            #we want to convert this min heap to a max heap so that we are popping off the farthest points in the case that size of the heap goes over k
            
            
            if len(heap) == K:
                #this first pushes the (dist, p) to the heap 
                #it then pops the largest distance off the heap 
                heapq.heappushpop(heap, (dist, p))
            else:
                #otherwise, if the heap size is smaller, then we want to just heappush to the heap 
                heapq.heappush(heap, (dist, p))
        return [p for (dist, p) in heap]

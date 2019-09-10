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


class Solution(object):
    def kClosest(self, points, K):
        import heapq
        heap = []
        for p in points:
            x, y = p[0], p[1]
            #get the euc distance 
            dist = -(x*x + y*y)
            
            #python heap is a min heap, we want to keep pushing distance to the heap with greatest distance at root until size is less than k and if it is already at the k size, we want to keep pushing the distance 
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, p))
            else:
                heapq.heappush(heap, (dist, p))
        return [p for (dist, p) in heap]

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        distance=0
        startpoint=points[0]
        for point in points[1:]:
            distance+=max(abs(startpoint[0]-point[0]),abs(startpoint[1]-point[1]))
            startpoint=point
        return distance

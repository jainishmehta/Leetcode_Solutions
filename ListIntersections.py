class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer=[]
        i=j=0
        while i<len(firstList) and j<len(secondList):
            hi=min(firstList[i][1], secondList[j][1])
            low=max(firstList[i][0], secondList[j][0])
            if low<=hi:
                answer.append([low, hi])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return answer

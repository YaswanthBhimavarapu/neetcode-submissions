class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        for i in range(len(heights)):
            for j in range(i+1 , len(heights)):
                width = j - i
                heigh = min(heights[i] , heights[j])
                area = width * heigh
                if maxi < area:
                    maxi = area

        return maxi
        
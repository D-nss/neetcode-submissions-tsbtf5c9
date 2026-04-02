class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # distancia = index
        # brute force = O(n^2)
        # maior index com maior tam
        # max(min(h1,h2)*d)
        
        res = 0
        l_pointer = 0
        r_pointer = len(heights) - 1
        while l_pointer < r_pointer:
            area = (min(heights[r_pointer], heights[l_pointer])*(r_pointer - l_pointer))
            res = max(res, area)
            if heights[r_pointer] > heights[l_pointer]:
                l_pointer += 1
            else:
                r_pointer -= 1
        
        return res

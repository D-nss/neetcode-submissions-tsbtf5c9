class Solution:
    def trap(self, height: List[int]) -> int:
        # percorrer a lista, h= 2, -> h>=2 (calcular altura), --alturas no caminho
        r,l = len(height) - 1, 0

        res = 0
        l_max = height[l]
        r_max = height[r]

        while l < r:
            if l_max < r_max:
                l +=1
                if l_max > height[l]:
                    res += l_max - height[l]
                    print(l_max - height[l])
                l_max = max(height[l], l_max)
            else:
                r -=1
                if r_max > height[r]:
                    res += r_max - height[r]
                    print(r_max - height[r])
                r_max = max(height[r], r_max)

        return res
                



class Solution:
    def findMin(self, nums: List[int]) -> int:
        [8,9,0,1,2,3,4,5,6]
        # nums[ini] > nums[fim]
        ini = 0
        fim = len(nums) -1

        if nums[ini] < nums[fim]:
            return nums[ini]

        while ini +1 < fim:
            media = ini + (fim - ini)//2
            if nums[ini] > nums[media]:
                fim = media
            else:
                ini = media
        
        return min([nums[ini], nums[fim]])
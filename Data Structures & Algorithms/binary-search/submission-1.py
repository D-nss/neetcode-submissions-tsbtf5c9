class Solution:
    def buscar(self, nums, ini, fim, target):
        meio =ini + (fim - ini)//2

        if nums[ini] == target:
            return ini
        
        if nums[fim] == target:
            return fim

        if fim - ini == 1 or fim - ini == 0:
            return -1
        
        elif nums[meio] > target:
            return self.buscar(nums, ini, meio, target)
        
        else:
            return self.buscar(nums, meio, fim, target)

    def search(self, nums: List[int], target: int) -> int:

        return self.buscar( nums, 0, len(nums) -1, target)
        


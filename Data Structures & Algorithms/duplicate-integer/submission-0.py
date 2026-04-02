class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        anterior = -1
        for i in nums:
            if i == anterior:
                return True
            anterior = i
        return False

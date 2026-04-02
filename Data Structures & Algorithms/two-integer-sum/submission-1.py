class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            outro_num = target - nums[i]
            for num in range(len(nums) - i -1):
                if nums[num + i +1] == outro_num:
                    return [i, num + i +1]
        return None


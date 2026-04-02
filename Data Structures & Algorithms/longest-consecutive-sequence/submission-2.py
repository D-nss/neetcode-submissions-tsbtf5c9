class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        anterior = -10**10
        nums.sort()
        lista = []
        for num in range(len(nums)):
            if nums[num] != anterior:
                lista.append(nums[num])
            anterior = nums[num]
        
        print(nums)
        maximo_local = 1
        maximo_geral = 1
        anterior = -10**10
        for num in lista:
            if num -1 == anterior:
                maximo_local +=1
            else:
                maximo_local = 1

            if maximo_local > maximo_geral:
                maximo_geral = maximo_local

            anterior = num

        return maximo_geral

        

            
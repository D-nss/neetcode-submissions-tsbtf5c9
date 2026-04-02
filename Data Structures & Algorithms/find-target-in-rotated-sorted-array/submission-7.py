class Solution:    
    def search(self, nums: List[int], target: int) -> int:
        inicio, fim = 0, len(nums) - 1
    
        while inicio <= fim:
            meio = (inicio + fim) // 2
            
            if nums[meio] == target:
                return meio
            
            if nums[inicio] <= nums[meio]:
                if nums[inicio] <= target < nums[meio]:
                    fim = meio - 1  
                else:
                    inicio = meio + 1 

            else:
                if nums[meio] < target <= nums[fim]:
                    inicio = meio + 1 
                else:
                    fim = meio - 1  
                    
        return -1 




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        dic = {}
        anterior = -10000
        for num in nums:
            if num == anterior:
                dic[num] += 1
            else: 
                dic[num] = 1
            
            anterior = num
        
        saida = []
        print(dic)
        for i in range(k):
            max_val = 0
            max_key = 0
            for key, val in dic.items():
                if val > max_val:
                    max_val = val
                    max_key = key
            
            dic[max_key] = 0

            saida.append(max_key)

        return saida
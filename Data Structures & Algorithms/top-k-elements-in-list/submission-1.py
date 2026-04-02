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
            maximo = max(dic, key=dic.get)
            
            dic[maximo] = 0

            saida.append(maximo)

        return saida
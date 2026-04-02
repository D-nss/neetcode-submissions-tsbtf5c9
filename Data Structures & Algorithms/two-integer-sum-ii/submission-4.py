class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
                dic[numbers[i]] = i

        for i in range(len(numbers)):
            procurado = target - numbers[i]
            if procurado in dic and numbers[i] != procurado:
                return[i +1, dic[procurado] +1]

        return []
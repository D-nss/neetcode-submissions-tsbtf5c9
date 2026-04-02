class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            numero_procurado = target - numbers[i]
            if numero_procurado != numbers[i]:
                print(numbers[i:])
                for num in range(len(numbers[i + 1:])):
                    if numbers[num + i + 1] == numero_procurado:
                        return [i +1, num + i + 2]
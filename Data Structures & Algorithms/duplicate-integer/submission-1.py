class Solution:
    def quickSort(self, lista)->List:
        if len(lista) <= 1:
            return lista

        pivot = lista[len(lista)//2]
        menor = []
        maior = []
        igual = []
        for i in lista:
            if i < pivot:
                menor.append(i)
            elif i > pivot:
                maior.append(i)
            else:
                igual.append(i)
        
        menor = self.quickSort(menor)
        maior = self.quickSort(maior)

        return menor + igual + maior

    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = self.quickSort(nums)
        anterior = -1
        for i in nums:
            if i == anterior:
                return True
            anterior = i
        return False

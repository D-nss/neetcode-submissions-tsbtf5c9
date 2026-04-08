class Solution:
    def quick_sort(self, index, lista):
        if len(lista) <= 1:
            return lista

        ini = []
        meio = []
        fim = []

        for i in lista:
            if i > lista[index]:
                fim.append(i)
            elif i < lista[index]:
                ini.append(i)
            else:
                meio.append(i)

        return self.quick_sort(len(ini)//2,ini) + meio + self.quick_sort(len(fim)//2, fim)


    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(len(nums)//2, nums)

        
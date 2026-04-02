class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zero = 0
        for i in nums:
            if i != 0:
                mult *=i
            else:
                zero += 1
        saida = []
        for i in nums:
            if zero == 1:
                if i != 0:
                    saida.append(0)
                else:
                    saida.append(mult)
            elif zero > 1:
                saida.append(0)

            else:
                saida.append(mult//i)

        return saida


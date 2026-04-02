class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # can it be -> ""?
        # can len(s2) < len(s1)?

        # Brute force -> vejo cada letra de s2, se for uma letra em s1 vemos se aproxima também é, se sim para len(s1) retornamos true se não seguimos ate retornar false
        # O(n*m) -> O(n^2)

        # 2 ponteiros -> l,r, se s2[l] in s1 and dic1[s2[l]] > 0, r+=1, if r-l+1 == len(s1) -> true, else: localizacao[]
        # letras podem se repetir
        
        l, r = 0, 0
        dic1 = {}

        for letra in s1:
            if letra in dic1:
                dic1[letra] += 1
            else:
                dic1[letra] = 1

        while r < len(s2):
            if s2[r] in dic1:
                if dic1[s2[r]] > 0:
                    dic1[s2[r]] -= 1
                    if r - l + 1 == len(s1):
                        return True  
                else:
                    for i in range(l, r):
                        if s2[l] == s2[r]:
                            l +=1
                            if r - l + 1 == len(s1):
                                return True
                            break
                        dic1[s2[l]] += 1
                        l +=1
                r += 1
            else:
                for i in range(l, r):
                    dic1[s2[l]] += 1
                    l +=1
                r += 1
                l = r
                
        return False







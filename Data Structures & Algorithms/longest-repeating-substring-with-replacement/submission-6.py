class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        lista = []
        max_letra = 0
        l, r = 0, 0
        dic = {}
        letras = set(s)
        for letra in letras:
            dic[letra] = 0
        
        while r< len(s):
            dic[s[r]] += 1
            print(dic)
            for i, val in dic.items():
                max_letra = max(val, max_letra)
            if r - l - max_letra + 1 <= k:
                res = max(res, r- l +1)
            else:
                while r - l - max_letra + 1 > k:
                    dic[s[l]] -= 1
                    print(dic)
                    l += 1
                    for i, val in dic.items():
                        max_letra = max(val, max_letra)
            r += 1
        return res
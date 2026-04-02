class Solution:
    def isPalindrome(self, s: str) -> bool:
        palavra = []
        for carac in s:
            if 65 <= ord(carac) and ord(carac) <= 90:   
                palavra.append(carac.lower())

            if 97 <= ord(carac) and ord(carac) <= 122:   
                palavra.append(carac.lower())

            if 48 <= ord(carac) and ord(carac) <= 57:   
                palavra.append(carac.lower())
        

        tam = len(palavra) -1
        count = 0

        while tam > count:
            if palavra[tam] != palavra[count]:
                return False
            tam -= 1
            count +=1
        
        return True

        
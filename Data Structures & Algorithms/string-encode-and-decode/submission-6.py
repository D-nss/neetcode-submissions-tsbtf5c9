class Solution:

    def encode(self, strs: List[str]) -> str:
        string_final = ''

        for palavra in strs:
                tam = len(palavra)
                string_final += str(tam) + '#'
                string_final += palavra

        
        string_final += '0'
        return(string_final)

    def decode(self, s: str) -> List[str]:
        saida = []
        count = 0
        num = ''
        for i in s[count:]:
                if i == '#':
                    break
                num += i
                count += 1
        start = int(num)

        while count < len(s) -1:
            if start == 0:
                palavra = ""
            else:
                palavra = ''
                for i in range(start):
                    count += 1
                    palavra += s[count]
            num = ''
            count += 1

            print(palavra)
            for i in s[count:]:
                if i == '#':
                    break
                num += i
                count += 1

            print(num)

            start = int(num)
            saida.append(palavra)
        
        return saida


        


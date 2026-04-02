class Solution:
    def opera(self, val1, val2, ope) -> int:
        if ope == '+':
            return val1 + val2

        if ope == '-':
            return val1 - val2

        if ope == '*':
            return val1 * val2
        
        if ope == '/':
            saida = ''
            for i in str(val1 / val2):
                if i == '.':
                    return int(saida)
                else:
                    saida += i
            return int(str(val1 / val2)[0])


    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        saida = 0
        for  i in tokens:
            if len(i)>1 or 48 <= ord(i)<= 57:
                num = i
                stack.append(int(num))
                print(stack)
            else:
                saida = self.opera(stack[-2], stack[-1], i)
                stack.pop()
                stack.pop()
                stack.append(saida)
                print(stack)
        return stack[0]
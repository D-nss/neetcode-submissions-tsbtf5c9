class TimeMap:

    def __init__(self):
        self.dic = {}
    
    def busca_bin(self, ini, fim, lista, target):
        print(ini, fim)
        if ini + 1 < fim:
            mid = (ini + fim)//2

            if lista[mid][1] == target:
                return lista[mid][0]
            
            if target > lista[mid][1]:
                return self.busca_bin(mid, fim, lista, target)
            else:
                return self.busca_bin(ini, mid, lista, target)
        else:
            print('fim')
            if target < lista[ini][1]:
                return ''
            elif target == lista[ini][1] or target < lista[fim][1]:
                return lista[ini][0]
            else:
                return lista[fim][0]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append([value, timestamp])
        else:
            self.dic[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.dic:
            return self.busca_bin(0, len(self.dic[key]) - 1, self.dic[key], timestamp)
        else:
            return ''


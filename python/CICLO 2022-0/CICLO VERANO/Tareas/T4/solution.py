class Solution():
    data = {}

    def __init__(self, file_name='data.csv'):
        """Read file"""
        with open(file_name) as file:
            mat = [i.split(",") for i in file.read().split("\n")]
        self.data = {i[0]: dict(zip(mat[0][1:], i[1:])) for i in mat[1:]}

    def ejercicio1(self):
        paises = {}
        for elemento in self.data.values():
            if elemento["country"] not in paises.keys():
                paises.update({elemento["country"]: 1})
            else:
                paises[elemento["country"]] += 1
        return paises

    def ejercicio2(self, id, camino):
        conexiones = []  # lista con los identificadores de las personas.
        dic = {'B': 'bestie', 'M': 'mom', 'D': "dad"}

        for i in camino:
            if self.data[id][dic[i]] == '':
                return conexiones, {}
            conexiones.append(self.data[id][dic[i]])
            id = self.data[id][dic[i]]

        # diccionario con la persona encontrada.
        persona_buscada = self.data[id]
        return conexiones, persona_buscada


s = Solution()
print(s.ejercicio1())

seq, info = s.ejercicio2("C18", "MMBD")
print(seq == ["B06", "A05", "B05", "A07"])
print(info == s.data["A07"])

seq, info = s.ejercicio2("D04", "DDBBMM")
print(seq == ["C04", "B01", "A12", "B13", "A11"])
print(info == {})

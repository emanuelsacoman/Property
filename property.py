class Matriz:
    def __init__(self, dimensao, data, tipo):
        self.dimensao = dimensao
        self.data = data
        self.tipo = tipo

    @property
    def dimensao(self):
        return self._dimensao

    @dimensao.setter
    def dimensao(self, valor):
        if isinstance(valor, tuple) and len(valor) == 2:
            self._dimensao = valor
        else:
            print("A dimensão deve ser uma tupla com dois valores.")

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, valor):
        if isinstance(valor, list) and all(isinstance(row, list) for row in valor):
            self._data = valor
        else:
            print("Os dados devem ser uma lista de listas.")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor):
        if valor in ["inteiro", "decimal", "complexo"]:
            self._tipo = valor
        else:
            print("O tipo deve ser 'inteiro', 'decimal' ou 'complexo'.")

    def __add__(self, outra_matriz):
        if self.dimensao == outra_matriz.dimensao and self.tipo == outra_matriz.tipo:
            resultado_data = []
            for i in range(self.dimensao[0]):
                linha_resultado = []
                for j in range(self.dimensao[1]):
                    soma = self.data[i][j] + outra_matriz.data[i][j]
                    linha_resultado.append(soma)
                resultado_data.append(linha_resultado)
            return Matriz(self.dimensao, resultado_data, self.tipo)
        else:
            print("As matrizes não podem ser somadas devido a diferenças na dimensão ou tipo.")
            return None

    def __mul__(self, outra_matriz):
        if self.dimensao[1] == outra_matriz.dimensao[0] and self.tipo == outra_matriz.tipo:
            resultado_data = []
            for i in range(self.dimensao[0]):
                linha_resultado = []
                for j in range(outra_matriz.dimensao[1]):
                    produto = 0
                    for k in range(self.dimensao[1]):
                        produto += self.data[i][k] * outra_matriz.data[k][j]
                    linha_resultado.append(produto)
                resultado_data.append(linha_resultado)
            return Matriz((self.dimensao[0], outra_matriz.dimensao[1]), resultado_data, self.tipo)
        else:
            print("As matrizes não podem ser multiplicadas devido a diferenças na dimensão ou tipo.")
            return None

    def __str__(self):
        matriz_str = ""
        for linha in self.data:
            matriz_str += " ".join(map(str, linha)) + "\n"
        return matriz_str

# Exemplo de uso:
matriz1 = Matriz((2, 2), [[1, 2], [3, 4]], "inteiro")
matriz2 = Matriz((2, 2), [[2, 3], [4, 5]], "inteiro")

resultado_soma = matriz1 + matriz2
resultado_multiplicacao = matriz1 * matriz2

print("Resultado da soma das matrizes:")
print(resultado_soma)

print("Resultado da multiplicação das matrizes:")
print(resultado_multiplicacao)

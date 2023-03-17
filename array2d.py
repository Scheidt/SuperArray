class SuperMatriz:
    def __init__(self, i: int, j: int) -> None:
        self.num_de_linhas = i
        self.num_de_colunas = j
        self.matriz = [None]*(i*j)

    def acessa(self, i: int, j: int):
        return self.matriz[(i-1)*self.num_de_colunas+j-1]

    def atribui(self, i: int, j: int, conteudo):
        self.matriz[(i-1)*self.num_de_colunas+j-1] = conteudo

mat = SuperMatriz(3, 4)
mat.atribui(1, 1, 66)
mat.acessa(1, 1)
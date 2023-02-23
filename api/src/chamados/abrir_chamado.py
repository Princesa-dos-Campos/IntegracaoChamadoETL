import pandas as pd

class AbrirChamado:
    def __init__(self,dados):
        # self.dados = pd.read_csv('chamados/Chamado.csv', encoding='ISO8859-1', sep=';')
        self.dados = dados
        print(self.dados)
        # self.separar_dados()

    def separar_dados(self):
            matriz = self.dados['dados'][2]
            # print(matriz)
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                        print(matriz[i][j])
            # matriz = len(self.dados['dados'])-1
            # print(matriz)
            # lista = self.dados['dados'][i]
            # print(lista)
            #definir for para pegar linha a linha do formulario
            # print(self.dados)



if __name__ == "__main__":
    from abrir_chamado import AbrirChamado
    AbrirChamado()
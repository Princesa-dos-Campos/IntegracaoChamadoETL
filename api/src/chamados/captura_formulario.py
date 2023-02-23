import pandas as pd

class CapturaFormulario:
    def __init__(self,dados):
        # self.dados = pd.read_csv('chamados/Chamado.csv', encoding='ISO8859-1', sep=';')
        self.dados = dados
        # print(self.dados)
        self.separar_dados()

    def separar_dados(self):
        try:
            matriz = self.dados['dados']
            # linha = len(matriz)
            for i in matriz:
                print("Informação I: ",i)
                for j in i:
                    print("Informação de J: ",j)
        except Exception as e:
            print('Erro ao abrir chamado...', e)
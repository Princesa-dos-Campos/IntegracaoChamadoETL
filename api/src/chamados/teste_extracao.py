#extrai dados do formulario por valor de coluna

class TesteExtracao():
    def __init__(self, df):
        self.df = df
        # print(self.df)
        self.extracao()

    def extracao(self):
        try:
            lista = []
            for i in self.df['formulario']:
                # print(i)
                lista = i
            # print(lista[1])
        except Exception as e:
            print("Erro na extração do formulario...", e)
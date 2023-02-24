import pandas as pd

class CapturaFormulario:
    def __init__(self,dados, form):
        # self.dados = pd.read_csv('chamados/Chamado.csv', encoding='ISO8859-1', sep=';')
        self.dados = dados
        self.form = form
        self.teste_form()
        # self.separar_dados()


    def teste_form(self):
        for ele in self.form:
            for id in self.form['id']:
                id_form = id
                for i in self.form['dados']:
                    ultimo = i[-1]
                    print("Ultimo:", ultimo)
                    for j in i:
                        print(j)
                        if j == ultimo:
                            print("igual ",id_form)






    def separar_dados(self):
        try:
            for i in self.form['dados']:
                flag  = 0
                for j in i:
                    ultimo_elemento = j[ -1]
                    for k in j:
                        if k == ultimo_elemento:
                            flag = 1
                            linha = j
                            print(linha)
                            print('ultimo: ', flag)
                if flag == 1:
                    break
        except Exception as e:
            print('Erro na captura do formulário...',e)

    # def separar_dados(self):
    #     """Separa linhas de chamado da string
    #     """
    #     try:
    #         matriz = self.dados['dados']
    #         for i in matriz:
    #             print("Informação I: ",i)
    #             for j in i:
    #                 print("Informação de J: ",j)
    #     except Exception as e:
    #         print('Erro ao abrir chamado...', e)
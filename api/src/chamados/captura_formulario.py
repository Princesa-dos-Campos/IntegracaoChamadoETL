from chamados.abrir_chamado import AbrirChamado
import pandas as pd
import numpy as np

class CapturaFormulario:
    def __init__(self,dados):
        # self.dados = pd.read_csv('chamados/Chamado.csv', encoding='ISO8859-1', sep=';')
        self.df = dados
        self.teste_form()


    def tentativa(self, chamado, titulo, empresa, requerente, andamento, responsavel, etapa, email, i):
        print('Entrou em tentativa...')
        nova_lista =[]
        lista_=[]
        nova_lista.append(chamado)
        nova_lista.append(titulo)
        nova_lista.append(empresa)
        nova_lista.append(requerente)
        nova_lista.append(andamento)
        nova_lista.append(responsavel)
        nova_lista.append(etapa)
        nova_lista.append(email)
        nova_lista.append(i)
        #envia nova lista p abrir chamado
        lista_.append(nova_lista)
        # print(lista_[0])
        df_chamado = pd.DataFrame(lista_, columns=['chamado', 'titulo', 'empresa', 'requerente', 'andamento', 'responsavel','etapa',
                                                        'email', 'dados'])
        # print(df_chamado)
        # df_chamado.to_csv(f'{chamado}.csv')
        AbrirChamado(df_chamado)



    def teste_form(self):
        try:
            tam = len(self.df)-1 #pegou quantidade de linhas do df
            while(tam>=0):
                # print(chamado,': ')
                for i in self.df['dados'][tam]:
                    etapa = str(self.df.iloc[tam]['etapa'])
                    chamado = str(self.df.iloc[tam]['chamado'])
                    empresa = str(self.df.iloc[tam]['empresa'])
                    requerente = str(self.df.iloc[tam]['requerente'])
                    titulo = str(self.df.iloc[tam]['titulo'])
                    andamento = str(self.df.iloc[tam]['andamento'])
                    responsavel = str(self.df.iloc[tam]['responsavel'])
                    email = str(self.df.iloc[tam]['email'])

                    self.tentativa(chamado, titulo, empresa, requerente, andamento, responsavel, etapa, email, i)
                tam-=1
            # print('Informações: ')
            # print(info)
        except Exception as e:
            print('Erro de captura...', e)


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
from chamados.testa_chamado import TestaChamado
import pandas as pd

class CapturaFormulario:
    def __init__(self,dados):
        self.df = dados
        # print(self.df)
        self.teste_form()

    def teste_form(self):
        try:
            lista_=[]
            r = 0
            tam = len(self.df)-1 #pegou quantidade de linhas do df
            while(tam>=0):
                for i in self.df['formulario'][tam]:
                    etapa = str(self.df.iloc[tam]['etapa'])
                    chamado = str(self.df.iloc[tam]['chamado'])
                    empresa = str(self.df.iloc[tam]['empresa'])
                    requerente = str(self.df.iloc[tam]['requerente'])
                    titulo = str(self.df.iloc[tam]['titulo'])
                    andamento = str(self.df.iloc[tam]['andamento'])
                    responsavel = str(self.df.iloc[tam]['responsavel'])
                    email = str(self.df.iloc[tam]['email'])
                    i = str(i)
                    lista_.append([etapa, chamado, empresa, requerente, titulo, andamento, responsavel, email, i])
                tam-=1
            df = pd.DataFrame(lista_, columns=['etapa', 'chamado', 'empresa', 'requerente', 'titulo', 'andamento', 'responsavel', 'email',
                                               'formulario'])
            df.to_csv('nova_lista.csv', sep=';', encoding="ISO-8859-1")
            # print(df)
            TestaChamado(df)
        except Exception as e:
            print('Erro de captura...', e)

import requests as req
from requests.auth import HTTPBasicAuth
import pandas as pd

class Extractor:
    def __init__(self, valor):
        self.username = 'integracao@princesadoscampos.com.br'
        self.password = '12345678'
        self.chamado = valor
        self.endpoint = f'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado/{self.chamado}'
        self.headers = {
            'Content-Type': 'application/json',
            'wtmh':'true'
        }
        self.execute()


    def execute(self):
        try:
            dados = []
            dados_ = []
            print('inicio execute extractor')
            data = req.get(url=self.endpoint, headers=self.headers, auth=HTTPBasicAuth(self.username, self.password)).json()
            print('resposta')
            tipo = data['tipo']
            etapa = data['etapa']
            categoria = data['categoria']
            empresa = data['empresa']
            requerente = data['requerente']
            email = data['email_requerente']
            responsavel = data['responsavel']
            aprovador = data['aprovador']
            chamado = data['numero']
            andamento = data['andamento']
            titulo = data['titulo']
            form = data['form']['jsons'][1]['fields'][0]['field_options']['data']
            print('fim resposta')
            dados.append(tipo)
            dados.append(etapa)
            dados.append(categoria)
            dados.append(empresa)
            dados.append(requerente)
            dados.append(email)
            dados.append(responsavel)
            dados.append(aprovador)
            dados.append(chamado)
            dados.append(andamento)
            dados.append(titulo)
            dados.append(form)

            dados_.append(dados)
            print('append dados2')
            tabela_chamado = pd.DataFrame(dados_, columns= ['Tipo', 'Etapa', 'Categoria', 'Empresa', 'Requerente', 'Email', 'Responsavel', 'Aprovador', 'Chamado', 'Andamento', 'Titulo', 'Conteudo'])
            print('criando excel')
            print(tabela_chamado)
            tabela_chamado.to_excel('Chamado.xlsx')
            print('excel criado')
        except Exception as e:
            return ('Erro' + str(e))

    # @property
    # def get_resp(self):
    #     return self.__resp

    # @__chamado.setter
    # def __chamado(self, chamado):
    #     if chamado != '':
    #         self.__chamado = chamado
    #     else:
    #         return 'Número de chamado inválido'
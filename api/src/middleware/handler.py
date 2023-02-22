import requests as req
from requests.auth import HTTPBasicAuth
import pandas as pd

class Handler:
    def __init__(self, lista):
        self.username = 'integracao@princesadoscampos.com.br'
        self.password = '12345678'
        self.lista = lista
        # print(self.lista)
        # self.endpoint = f'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado/{self.chamado}'
        self.headers = {
            'Content-Type': 'application/json',
            'wtmh':'true'
        }
        self.execute()


    def execute(self):
        try:
            dados_ = []
            for chamado in self.lista:
                print('Manipulando dados do chamado: ',chamado)
                dados = []
                endpoint = f'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado/{chamado}'
                data = req.get(url=endpoint, headers=self.headers, auth=HTTPBasicAuth(self.username, self.password)).json()
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

            dados_ = pd.DataFrame(dados_, columns=['tipo', 'etapa','categoria', 'empresa', 'requerente', 'email', 'responsavel',
                                                    'aprovador', 'chamado','andamento','titulo', 'dados'])
            # print(dados_)
            print('Criando CSV...')
            dados_.to_csv('Chamado.csv', index=False, sep=';', encoding='ISO8859-1')
            print('CSV criado')

        except Exception as e:
            print('Erro na manipulação de dados...' + str(e))




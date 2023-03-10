import requests as req
from requests.auth import HTTPBasicAuth
import pandas as pd
from chamados.captura_chamado import CapturaChamado

class Handler:
    """
    Manipula os dados vindos da API
    """
    def __init__(self, lista):
        self.username = 'robo.dataentry@princesadoscampos.com.br'
        self.password = '12345678'
        self.lista = lista
        self.headers = {
            'Content-Type': 'application/json',
            'wtmh':'true'
        }
        self.execute()


    def execute(self):
        try:
            dados_ = []
            print("lista", self.lista)
            for chamado in self.lista:
                print('Manipulando dados do chamado: ',chamado)
                dados = []
                endpoint = f'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado/{chamado}'
                data = req.get(url=endpoint, headers=self.headers, auth=HTTPBasicAuth(self.username, self.password)).json()

                tipo = data['tipo']
                etapa = data['etapa']
                empresa = data['empresa']
                requerente = data['requerente']
                email = data['email_requerente']
                responsavel = data['responsavel']
                aprovador = data['aprovador']
                chamado = data['numero']
                andamento = data['andamento']
                titulo = data['titulo']
                formulario = data['form']['jsons'][0]['fields'][0]['field_options']['data']

                dados.append(tipo)
                dados.append(etapa)
                dados.append(empresa)
                dados.append(requerente)
                dados.append(email)
                dados.append(responsavel)
                dados.append(aprovador)
                dados.append(chamado)
                dados.append(andamento)
                dados.append(titulo)
                dados.append(formulario)

                dados_.append(dados)

            dados_ = pd.DataFrame(dados_, columns=['tipo', 'etapa', 'empresa', 'requerente', 'email', 'responsavel', 'aprovador',
                                                   'chamado','andamento','titulo', 'formulario'])
            print('Criando CSV...')
            dados_.to_csv('Chamado.csv', index=True, sep=';', encoding='ISO8859-1')
            print('CSV criado')
            # print(dados_)
            CapturaChamado(dados_)
        except Exception as e:
            print('Erro na manipula????o de dados...' + str(e))

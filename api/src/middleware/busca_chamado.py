import requests as req
from requests.auth import HTTPBasicAuth
from middleware.extractor import Extractor

class BuscaChamado:
    """ Classe para fazer conexão com a API (Consulta caixa de entrada), com email do usuário. Chama classe Handler.
        Return: Dados inbox(data), total de chamados no inbox(total_chamados)
    """

    def __init__(self):
        self.username = 'robo.dataentry@princesadoscampos.com.br'
        self.pwd = '12345678'
        self.email = 'robo.dataentry@princesadoscampos.com.br'
        self.endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/workflow/entrada'
        self.headers = {
            'Content-Type': 'application/json',
            'wtmh': 'true'
        }
        self.body = {
            "usuario_email": "robo.dataentry@princesadoscampos.com.br",
            "page": 0
        }
        self.execute()

    def execute(self):
        print('Iniciando')
        try:
            # print('try')
            data = req.get(url=self.endpoint, headers=self.headers, json=self.body, auth=HTTPBasicAuth(self.username, self.pwd)).json()
            total_chamados = data['total_chamados'] #(-1)
            data = data['chamados_encontrados']
            # print(data[6]['tipo_chamado'])
            # print(total_chamados)
            Extractor(data, total_chamados)
        except Exception as e:
            return ('Erro' + str(e))
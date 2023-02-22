import requests as req
from requests.auth import HTTPBasicAuth
from middleware.handler import Handler

class BuscaChamado:
    """ Classe para fazer conexão com a API (Consulta caixa de entrada), com email do usuário. Chama classe Handler.
        Return: Dados inbox(data), total de chamados no inbox(total_chamados)
    """

    def __init__(self):
        self.username = 'integracao@princesadoscampos.com.br'
        self.pwd = '12345678'
        self.email = 'gustavo.trudes@princesadoscampos.com.br'
        self.endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/workflow/entrada'
        self.headers = {
            'Content-Type': 'application/json',
            'wtmh': 'true'
        }
        self.body = {
            "usuario_email": "gustavo.trudes@princesadoscampos.com.br",
            "page": 0
        }
        self.execute()

    def execute(self):
        print('Busca de Chamado')
        try:
            data = req.post(url=self.endpoint, headers=self.headers, json=self.body, auth=HTTPBasicAuth(self.username, self.pwd)).json()
            # Handler(data)
            # print('antes print')
            total_chamados = data['total_chamados'] #(-1)
            data = data['chamados_encontrados']
            # print(data[6]['tipo_chamado'])
            # print(total_chamados)
            Handler(data, total_chamados)
        except Exception as e:
            return ('Erro' + str(e))
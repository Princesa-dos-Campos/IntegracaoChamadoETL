import requests as req
from requests.auth import HTTPBasicAuth

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
            # print('fim extractor')
            resp = req.get(url=self.endpoint, headers=self.headers, auth=HTTPBasicAuth(self.username, self.password)).json()
            return resp
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
import requests as req
from requests.auth import HTTPBasicAuth

class Extractor:
    def __init__(self, valor):
        self.username = 'integracao@princesadoscampos.com.br'
        self.password = '12345678'
        self.__chamado = valor
        self.endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado/{self.chamado}'
        self.headers = {
            'Content-Type': 'application/json',
            'wtmh':'true'
        }
        self.__resp = self.execute()


    def execute(self):
        try:
            print('fim')
            return req.get(url=self.endpoint, headers=self.headers, auth=HTTPBasicAuth(self.username, self.password)).json()
        except Exception as e:
            return ('Erro' + str(e))

    @property
    def resp(self):
        return self.__resp

    @__chamado.setter
    def __chamado(self, chamado):
        if chamado != '':
            self.__chamado = chamado
        else:
            return 'Número de chamado inválido'
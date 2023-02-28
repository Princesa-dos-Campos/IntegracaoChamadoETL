import json
import requests as req
from requests.auth import HTTPBasicAuth

class AbreChamado():
    def __init__(self, dados):
        self.df = dados
        self.username = 'integracao@princesadoscampos.com.br'
        self.password = '12345678'
        self.proxy = {
            'http':'http://proxy.princesadoscampos.local:3128'
        }
        self.headers = {
            'Content-Type' :'application/json',
            'wtmh-debug': 'true'
        }
        self.endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado'
        self.integracao_wtmh()

    def integracao_wtmh(self):
        try:
            tam = len(self.df)-1
            while tam >=0:
                mensagem = "Dados: "+self.df['dados'][tam]
                body = {
                    "tipo_chamado": "CR.054 - Conferencia de ficha de remessa",
                    "empresa_relacionada": "EPC-ADM-MATRIZ-PR",
                    "requerente": self.df['email'][tam],
                    "titulo": "Dados do Formulario",
                    "mensagem": mensagem
                }
                body = json.dumps(body)
                resp = req.post(url = self.endpoint, headers= self.headers, data= body, auth=HTTPBasicAuth(self.username, self.password))
                retorno = resp.json()
                print(retorno)
                # chamado_novo = str(retorno['numero'])
                tam-=1
        except Exception as e:
            print("Erro ao abrir o chamado...", e)

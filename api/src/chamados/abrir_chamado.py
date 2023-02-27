import json
import requests as req
from requests.auth import HTTPBasicAuth
import pandas as pd

class AbrirChamado:
    def __init__(self, dados_chamado):
        self.df = pd.DataFrame(dados_chamado)
        # print(self.chamado)
        self.username = 'robo.dataentry@princesadoscampos.com.br'
        self.pwd = '12345678'
        self.headers = {
            'Content-Type':'application/json',
            'wtmh-debug':'true'
        }
        self.proxies = {
            'http':'http://proxy.princesadoscampos.local:3128'
        }
        self.integracao_chamado()


    def integracao_chamado(self):
        try:
            dados = []
            for chamado in self.df['chamado']:
                chamado = chamado
            for dados in self.df['dados']:
                dados = dados
            for empresa in self.df['empresa']:
                empresa = empresa
            # print(chamado, dados, empresa)
            endpoint = f'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado/'
            mensagem = "Dados referentes ao chamado:"+chamado+" Empresa:"+empresa+"Dados:"+str(dados)
            body ={
                 "acao":"atender",
                 "numero": chamado,
                "mensagem": mensagem
            }
            teste = json.dumps(body)
            body = json.dumps(body)
            resp = req.put(url = endpoint,headers=self.headers,data = body,auth = HTTPBasicAuth(self.username, self.pwd))
            retorno = resp.json()
            print(retorno)
        except Exception as e:
            print('Erro na integração de chamado...',e)
            #cria dados p retorno caso tenha algum campo vazio
            #deu certo porem o msm chamado n pode ser atendido mais de uma vez

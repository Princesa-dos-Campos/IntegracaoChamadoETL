import json
import requests as req
from requests.auth import HTTPBasicAuth
import pandas as pd
from chamados.abre_chamado import AbreChamado

class TestaChamado:
    def __init__(self, dados_chamado):
        self.df = pd.DataFrame(dados_chamado)
        self.endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado'
        self.username = 'robo.dataentry@princesadoscampos.com.br'
        self.pwd = '12345678'
        self.headers = {
            'Content-Type':'application/json',
            'wtmh-debug':'true'
        }
        self.proxies = {
            'http':'http://proxy.princesadoscampos.local:3128'
        }
        # print(self.df)
        self.integracao_chamado()

    def integracao_chamado(self):
        try:
            tam = len(self.df)-1
            while tam >=0:
                # self.df['dados'][tam]
                mensagem = 'Dados: '+self.df['dados'][tam]
                body = {
                    'acao': 'atender',
                    'numero': self.df['chamado'][tam],
                    'mensagem': mensagem
                }
                body = json.dumps(body)
                tam-=1
                resp = req.put(url = self.endpoint,headers=self.headers,data = body,auth = HTTPBasicAuth(self.username, self.pwd))
                retorno = resp.json()
                print(retorno)
            AbreChamado(self.df)
        except Exception as e:
            print('dados invalidos...',e)
            mensagem = "Dados inválidos"
            body={
                "acao":"retorno",
                "numero":self.df['chamado'],
                "mensagem": mensagem
            }









    # def integracao_chamado(self):
    #     try:
    #         dados = []
    #         endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado'
    #         mensagem = "Dados:"+str(dados)
    #         body ={
    #             "acao":"atender",
    #             "numero": self.df['chamado'],
    #             "mensagem": mensagem
    #         }
    #         body = json.dumps(body)
    #         resp = req.put(url = endpoint,headers=self.headers,data = body,auth = HTTPBasicAuth(self.username, self.pwd))
    #         retorno = resp.json()
    #         print(retorno)
    #             # abrir(self.df)
    #     except Exception as e:
    #         mensagem = "Dados inválidos"
    #         body={
    #             "acao":"retorno",
    #             "numero":self.df['chamado'],
    #             "mensagem": mensagem
    #         }
    #         print('Dados invalidos...', e)
            #cria dados p retorno caso tenha algum campo vazio
            #deu certo porem o msm chamado n pode ser atendido mais de uma vez
            #testar aqui se vai ser possivel atender ou nao (campos vazios), se for possivel ai sim encaminha p abrir o chamado

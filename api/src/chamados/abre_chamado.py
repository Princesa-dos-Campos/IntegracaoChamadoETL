import json
import requests as req
from requests.auth import HTTPBasicAuth
from log import Log

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
        # print(self.df['fornecedor'])
        try:
            tam = len(self.df)-1
            while tam >=0:
                # print(self.df['fornecedor'][tam])
                mensagem = "Cód.Fornecedor: "+self.df['fornecedor'][tam]+" Código: "+self.df['codigo'][tam]+" Nome da Agência(Vendedor): "+self.df['agencia_vendedor'][tam]+" Razão Social: "+self.df['razao_social'][tam]+" CNPJ: "+self.df['cnpj'][tam]+" Ano: "+self.df['ano'][tam]+" Valor NF: "+self.df['valor_nf'][tam]+" Data Vencimento: "+self.df['data_pgmt'][tam]+" Natureza: "+self.df['natureza'][tam]+" Email: "+self.df['email'][tam]
                body = {
                    "tipo_chamado": "CR.054 - Conferencia de ficha de remessa",
                    "empresa_relacionada": "EPC-ADM-MATRIZ-PR",
                    "titulo": "Data de Vencimento: "+self.df['data_pgmt'][tam],
                    "mensagem": mensagem
                }
                body = json.dumps(body)
                resp = req.post(url = self.endpoint, headers= self.headers, data= body, auth=HTTPBasicAuth(self.username, self.password))
                retorno = resp.json()
                print(retorno)
                Log()
                tam-=1
        except Exception as e:
            print("Erro ao abrir o chamado...", e)

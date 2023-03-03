import pandas as pd
from chamados.abre_chamado import AbreChamado

#extrai dados do formulario por valor de coluna

class TesteExtracao():
    def __init__(self, df):
        self.df = df
        # print(self.df)
        self.extracao()

    def extracao(self):
        try:
            lista = []
            serie = self.df['formulario']
            # print(type(serie))
            for linha in serie:
                # print("dados por linha: ",linha)
                linha = linha.strip("']'")
                linha = linha[2:]
                linha = linha.split("', '")
                empresa = linha[0]
                fornecedor = linha[1]
                codigo = linha[2]
                agencia = linha[3]
                razao = linha[4]
                cnpj = linha[5]
                ano = linha[6]
                nf = linha[7]
                data = linha[8]
                natureza = linha[9]
                email = linha[10]
                custo = linha[11]
                servico = linha [12]
                lista.append([empresa, fornecedor, codigo, agencia, razao, cnpj, ano, nf, data, natureza, email, custo, servico])
            formulario = pd.DataFrame(lista, columns=["empresa", "fornecedor", "codigo", "agencia_vendedor", "razao_social", "cnpj", "ano", "valor_nf", "data_pgmt", "natureza", "email",
                                                      "custo", "servico"])
            # print(formulario)
            # TestaChamado(formulario)
            AbreChamado(formulario)
        except Exception as e:
            print("Erro na extração do formulario...", e)
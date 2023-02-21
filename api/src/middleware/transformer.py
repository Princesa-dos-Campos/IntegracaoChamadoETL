import pandas as pd

class Transformer:
    def __init__(self, resp):
        self.data = resp
        print(resp)
        # self.execute()

    def execute(self):
        dados = []
        dados_ = []
        tipo = self.data['tipo']
        etapa = self.data['etapa']
        categoria = self.data['categoria']
        empresa = self.data['empresa']
        requerente = self.data['requerente']
        email = self.data['email_requerente']
        responsavel = self.data['responsavel']
        aprovador = self.data['aprovador']
        chamado = self.data['numero']
        andamento = self.data['andamento']
        titulo = self.data['titulo']
        form = self.data['form']['jsons'][1]['fields'][0]['field_options']['data']

        dados.append(tipo)
        dados.append(etapa)
        dados.append(categoria)
        dados.append(empresa)
        dados.append(requerente)
        dados.append(email)
        dados.append(responsavel)
        dados.append(aprovador)
        dados.append(chamado)
        dados.append(andamento)
        dados.append(titulo)
        dados.append(form)

        dados_.append(dados)
        tabela_chamado = pd.DataFrame(dados_, columns= ['Tipo', 'Etapa', 'Categoria', 'Empresa', 'Requerente', 'Email', 'Responsavel', 'Aprovador', 'Chamado', 'Andamento', 'Titulo', 'Conteudo'])
        tabela_chamado.to_excel('chamado.xlsx')
        print('fim transformer')
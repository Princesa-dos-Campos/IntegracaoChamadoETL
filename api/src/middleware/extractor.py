from middleware.handler import Handler

class Extractor:
    """Classe para navegar pelos dados em json vindos da classe BuscaChamado, fazendo a busca pelo chamado correspondente pelo
    campo 'tipo_chamado'. Chama classe Extractor.
       Return: Número do chamado ('numero')
    """
    def __init__(self, data, total_chamados):
        self.data = data
        self.total_chamados = total_chamados
        # print(self.total_chamados)
        # print(self.data)
        self.search()

    def search(self):
        try:
            print('Extraindo chamados da caixa de entrada...')
            cont = 0
            lista = []
            # print(self.data[2]['tipo_chamado'])
            # print(self.total_chamados, cont)
            while(cont < self.total_chamados):
                if(self.data[cont]['tipo_chamado'] == 'TI.072 - Desenvolvimento robôs'):
                    # print(self.data[cont]['tipo_chamado'])
                    chamado = self.data[cont]['numero']
                    # print(chamado)
                    lista.append(chamado)
                cont += 1
            print('fim while')
            # print(lista)
            Handler(lista)
        except Exception as e:
            print('Erro na extração de chamado...' + str(e))


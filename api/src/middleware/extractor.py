from middleware.handler import Handler

class Extractor:
    """Classe para navegar pelos dados em json vindos da classe BuscaChamado, fazendo a busca pelo chamado correspondente pelo
    campo 'fluxo_chamado'. Chama classe Extractor.
       Return: Número do chamado ('numero')
    """
    def __init__(self, data, total_chamados):
        self.data = data
        self.total_chamados = total_chamados
        self.search()

    def search(self):
        try:
            print('Extraindo chamados da caixa de entrada...')
            cont = 0
            lista = []
            while(cont < self.total_chamados):
                if(self.data[cont]['fluxo_chamado'] == 'TI.072.2 - Disparo robo'):
                    chamado = self.data[cont]['numero']
                    lista.append(chamado)
                cont += 1
            Handler(lista)
        except Exception as e:
            print('Erro na extração de chamado...' + str(e))


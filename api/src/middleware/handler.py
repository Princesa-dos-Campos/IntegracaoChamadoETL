from middleware.extractor import Extractor

class Handler:
    """Classe para navegar pelos dados em json vindos da classe BuscaChamado, fazendo a busca pelo chamado correspondente pelo
    campo 'tipo_chamado'. Chama classe Extractor.
       Return: Número do chamado ('numero')
    """
    def __init__(self, data, total_chamados):
        self.data = data
        self.total_chamados = total_chamados
        self.search()

    def search(self):
        print('Consultando Caixa de Entrada...')
        cont = 0
        lista = []
        while(cont < self.total_chamados):
            if(self.data[cont]['tipo_chamado'] == 'TI.072 - Desenvolvimento robôs'):
                chamado = self.data[cont]['numero']
                lista.append(chamado)
            cont += 1
        Extractor(lista)

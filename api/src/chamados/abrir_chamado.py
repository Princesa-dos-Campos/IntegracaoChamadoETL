class AbrirChamado:
    def __init__(self, dados):
        self.dados = dados
        # print(self.dados)
        self.separar_dados()

    def separar_dados(self):
        for linha in self.dados:
            chamado = self.dados['chamado']
            #definir for para pegar linha a linha do formulario
            dados = self.dados['dados'][]
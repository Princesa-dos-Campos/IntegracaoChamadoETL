from middleware.extractor import Extractor
from middleware.busca_chamado import BuscaChamado
#'20230217113892'
def job():
    # print('Rotina Robô - ETL Inicializado')
    # print('Extraindo dados')
    # Extractor('20230217113892')
    BuscaChamado()


if __name__ == "__main__":
    job()

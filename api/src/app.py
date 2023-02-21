from middleware.extractor import Extractor
from middleware.transformer import Transformer

#'20230217113892'
def job():
    print('Rotina Robô - ETL Inicializado')
    print('Extraindo dados')
    resp = Extractor('20230217113892')
    print(resp)


if __name__ == "__main__":
    job()

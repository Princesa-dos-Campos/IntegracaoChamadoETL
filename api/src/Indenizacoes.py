import requests as req
from requests.auth import HTTPBasicAuth
import json
import pandas as pd
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime

# username = 'amanda.ferreira@princesadoscampos.com.br'
# password = 'amanda16'

# username = ''
# password = '42650323'

username = 'bruno.silva@princesadoscampos.com.br'
password = '260598'

tabela = pd.read_excel('indenizacoes.xlsx')
tabela = pd.DataFrame(tabela)
print(tabela)

proxies = {
    'http':'http://proxy.princesadoscampos.local:3128'
}

headers = {
        'Content-Type' :'application/json',
        'wtmh-debug': 'true'
    }
desti = username #'gustavo.trudes@princesadoscampos.com.br'#
#endpoint = 'https://demo.wtmh.com.br/integracao/chamado/2022060655124'
endpoint = 'https://csc.princesadoscampos.wtmh.com.br/integracao/chamado'

def convert_data(data):
    data = str(data).split(' ')
    data = str(data[0]).split('-')
    ano = data[0]
    mes = data[1]
    dia = data[2]

    return dia+'/'+mes+'/'+ano

def enviar_email(tabela):
    registros = str(len(tabela))
    timestamp_now = datetime.timestamp(datetime.now())
    time_now = datetime.fromtimestamp(timestamp_now-10800)
    time_now = str(time_now).split('.')
    time_now = str(time_now[0])

    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    #Replace with your own gmail account
    gmail = 'automacao.wtmh@princesadoscampos.com.br'
    password = 'Awc432059'
    message = MIMEMultipart('mixed')
    message['From'] = 'Robô CSC - Descomplica <{sender}>'.format(sender = gmail)
    message['To'] =  desti 
    #message['CC'] = 'contact@company.com'
    message['Subject'] = 'Rotina Automática Chamado OP.005 - B'
    msg_content = """
    
    <body style="font-family: Arial, Helvetica, sans-serif;margin: 2px;">     
    <main style="background-color: rgb(255, 255, 255); border-radius: 10px;width: 100vw; height: 100vh;">
        <div style=" height: 50px; background-color: #025908;margin: 2px;">
            <img src="https://www.princesadoscampos.com.br/wp-content/themes/princesadoscampos/image/logo.png" style="height: 50px;">
        </div>            
        <div style="text-align: center;">
            <h1 style="font-size: 18px;color: #82BF56;">Rotina do Chamado OP.005 - B - Inclusão pagamento de titulo de indenização Finalizada</h1>
        </div>
        <div >
            <br>
            <div style="text-align:justify;">
                <p>Olá, a rotina do chamado OP.005 - B - Inclusão pagamento de titulo de indenização foi finalizada com """+registros+""" registros processados, segue em anexo o resumo dos envios pelo robô. </p>
                <br>
            </div> 
            <div style="text-align:left;"></div>
                <p>Att</p>
                <p>Equipe T.I. Expresso Princesa dos Campos</p>
            </div>
        </div> 
    </main>
</body>

    
    \n"""
    body = MIMEText(msg_content, 'html')
    message.attach(body)

    attachmentPath = "logs.xlsx"

    try:
        with open(attachmentPath, "rb") as attachment:
            p = MIMEApplication(attachment.read(),_subtype="xlsx")	
            p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
            message.attach(p)
    except Exception as e:
        print(str(e))

    msg_full = message.as_string()
    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()
        server.login(gmail, password)
        server.sendmail(gmail, str(message['To']).split(";"),msg_full)
        server.quit()

    print("Email Enviado Com Sucesso")

def integracao_wtmh():
    dados = []
    dados_=[]
#AQUI pega dados do dataframe ao inves da tabela
    for i in range(0,len(tabela)):
    #for i in range(0,5):
        cte = str(tabela.iloc[i][0])
        nome_fornecedor = str(tabela.iloc[i][1])
        cod_fornecedor = str(tabela.iloc[i][2])
        loja = str(tabela.iloc[i][3])
        valor_ = str(round(float(tabela.iloc[i][4]),2))
        vencimento = convert_data(str(tabela.iloc[i][5]))
        parcela = str(tabela.iloc[i][6])
        natureza = str(tabela.iloc[i][7])
        filial = str(tabela.iloc[i][8])
        centro_custo = str(tabela.iloc[i][9])

        dados.append(cte)
        dados.append(nome_fornecedor)
        dados.append(cod_fornecedor)
        dados.append(loja)
        dados.append(valor_)
        dados.append(vencimento)
        dados.append(parcela)
        dados.append(natureza)
        dados.append(filial)
        dados.append(centro_custo)

        mensagem = 'Favor incluir título no contas a pagar, CTE: '+cte+', Cod Fornecedor: '+cod_fornecedor+', Loja: '+loja+', '+nome_fornecedor+', Vencimento: '+vencimento+', Parcela: '+parcela+', Natureza: '+natureza+', Filial: '+filial+', Centro de Custo: '+centro_custo +', Valor: R$ '+valor_       

        #print(mensagem)

        body = {
            "tipo_chamado": "CR.054 - Conferencia de ficha de remessa",
            "empresa_relacionada": "EPC-ADM-MATRIZ-PR",
            "titulo": "CTE: "+cte +" Fornecedor: "+ nome_fornecedor+ ' '+ 'Vencimento: '+vencimento,
            "mensagem": mensagem
        }

        body = json.dumps(body)
        #print(mensagem)
        #print(dados)
        try:
            resp = req.post(url = endpoint,headers=headers,data = body,auth = HTTPBasicAuth(username, password))
            retorno = resp.json()
            print(retorno)
            chamado = str(retorno['numero'])
            dados.append(chamado)
            dados_.append(dados)
            dados = []
        except:
            msg = retorno['msg']
            print(msg)
            dados.append(msg)
            dados_.append(dados)
            dados=[]

    tabelafinal = pd.DataFrame(dados_,columns=[
    'CTE',	
    'NOME FORNECEDOR',
    'FORNECEDOR',
    'LOJA',
    'VALOR', 	
    'VENCIMENTO',	
    'PARCELA',	
    'NATUREZA',	
    'FILIAL',	
    'CENTRO DE CUSTO',
    'Chamado/Erro'])
    tabelafinal.to_excel('logs.xlsx')
    print(tabelafinal)
    enviar_email(tabelafinal)

integracao_wtmh()
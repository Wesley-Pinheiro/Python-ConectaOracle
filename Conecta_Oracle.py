#INICIO PROJETO
#conexao oracle

import cx_Oracle # para comunicar com o Oracle. No terminal -> (python -m pip install cx_Oracle --upgrade pip)  python -m yum -y install cx_Oracle

#Conexao Oracle
myCONNORA = cx_Oracle.connect('' + 'usuario_banco' + '/'+ 'senha_banco' + '@' + 'tnsnames_banco' +'') #conexao com o Oracle
myCONNORA.autocommit = True 
curORA = myCONNORA.cursor() #execucoes Oracle


#aqui se voce precisar mudar alguma variavel de ambiente para sua sessao, tipo: data / NLS_LANG / tipos numericos....
def alteraVARIAVEISDEAMBIENTE():
        curORA.execute("ALTER SESSION SET NLS_NUMERIC_CHARACTERS= ',.' ")

#aqui um modelo de select simples, colocar a query na variavel iQUERY
def selectSIMPLES():
        iQUERY = (" select * from NOME_DA_TABELA   "  )
        for iITEMS in curORA.execute(iQUERY).fetchall():  
                print(iITEMS[0]) #aqui ira mostrar a primeira coluna linha-a-linha

#aqui se voce quiser executar uma procedure
def executaPROCEDURE():
        curORA.callproc("AQUI O NOME DA PROCEDURE") 

#chamando a funcao para fazer consulta simples
selectSIMPLES()



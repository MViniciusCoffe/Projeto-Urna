from classes_urna import *

#Constantes
#=========================================#

CANDIDATOS = 1
REALIZAR_ELEICOES = 2
SAIR = VOLTAR = 0

#Constantes do menu inicial
#=========================================#

ADICIONAR_CANDIDATO = 1
ALTERAR_DADOS = 2
EXCLUIR_DADOS = 3
MOSTRAR_CANDIDATOS = 4

#Constantes do crud
#=========================================#

REALIZAR_ELEICAO = 1
FINALIZAR_ELEICAO = 2

#constandes da eleição
#=========================================#

#funções
def menu_inicial():
    print("""
================================================
>>                 URNA IFRN                  <<
================================================
>>   1.  Candidatos                           <<
>>   2.  Realizar eleição                     <<
>>   0.  Sair                                 <<
================================================""")
    return ''

def menu_crud():
    print("""
================================================
>>                 URNA IFRN                  <<
================================================
>>   1.  Adicionar candidato                  <<
>>   2.  Alterar dados                        <<
>>   3.  Excluir dados                        << 
>>   4.  Mostrar Candidatos                   <<              
>>   0.  Voltar                               <<
================================================""")
    return ''

def menu_eleicao():
    print("""
================================================
>>                 URNA IFRN                  <<
================================================
>>   1.  Realizar eleição                     <<
>>   2.  Finalizar eleição                    <<             
>>   0.  Voltar                               <<
================================================""")
    return ''

from classes_urna import *
from funcoes import *

menu_crud()
menu_eleicao()
menu_inicial()

urna = Urna()
candidato = Candidato('João alfredo', '123', 14)
candidato2 = Candidato('João', '143', 12)
candidato3 = Candidato('Alfredo', '121', 17)

try:
    urna.adicionar_candidato(candidato, 14)
    urna.adicionar_candidato(candidato2, 12)
    urna.adicionar_candidato(candidato3, 17)
    print('Candidato Adicionado com Sucesso')
except(CandidatoRepetidoException):
    print('O futuro é top')

novo_candidato = Candidato('Pedu Luçu', '323', 14)

if urna.verificar_numero(14):
    print('pão de batata')
else:
    print('jidhfkjsdhfa')

if urna.editar_candidato(novo_candidato, 14):
    print('lsafdjnon')
else:
    print('ljnf')


urna.deletar_candidato(14)

if urna.fazer_votacao(12) != 1:
    print(f'Você votou em {12}')
else:
    print('asjfdlsfdksfdalkçsklçsafdljkçsfdakkaljkçakkasdkfsdçkfajç')

if urna.fazer_votacao(11243) != 1:
    print(f'Você votou em {12}')
else:
    print('asjfdlsfdksfdalkçsklçsafdljkçsfdakkaljkçakkasdkfsdçkfajç')

if urna.fazer_votacao(-1) != -1:
    print(f'Você votou em {12}')
else:
    print('asjfdlsfdksfdalkçsklçsafdljkçsfdakkaljkçakkasdkfsdçkfajç')

for candidato in urna.candidatos:
    print(candidato)
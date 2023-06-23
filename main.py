from funcoes import *
from classes_urna import *
from os import *

urna = Urna()

while True:
    menu_inicial()
    opt = int(input('Digite uma opção: '))
    if opt == CANDIDATOS:
        while True:
            menu_crud()
            opt = int(input('Digite uma opção: '))
            
            if opt == ADICIONAR_CANDIDATO:
                #pede as informações do candidato
                nome = input('Digite seu nome: ')
                cpf = input('Digite seu CPF: ')
                numero = int(input('Digite seu número: '))

                #inicia a classe
                candidato = Candidato(nome, cpf, numero)

                #aqui ele tenta adicionar um usuário caso não tenha nenhum número repetido
                try:
                    urna.adicionar_candidato(candidato, numero)
                    print('Candidato adicionado com sucesso')
                    system('Pause')
                except(CandidatoRepetidoException):
                    print('Candidato já existente, por favor troque o número de campanha')
                    system('pause')

            elif opt == ALTERAR_DADOS:
                #verifica se há algum candidato na lista de candidatos
                if len(urna.candidatos) != 0:

                    numero = int(input('Digite o número do candidato: '))
                    
                    #verifica se o cpf está cadastrado
                    if urna.verificar_numero(numero):

                        #pede as informações do usuário de novo (o número ele não pode alterar)
                        novo_nome = input('Novo nome: ')
                        novo_cpf = input('Novo CPF: ')
                        #inicia a classe recebendo as novas informações (nome, cpf)
                        novo_candidato = Candidato(novo_nome, novo_cpf, numero)

                        urna.editar_candidato(novo_candidato, numero)
                        print('Candidato editado com sucesso')
                        system('Pause')
                        
                    else:
                        print('Candidato não existe')
                        system('pause')
                
                else:
                    print('Não existem candidatos cadastrados ainda')
                    system('pause')

            elif opt == EXCLUIR_DADOS:
                #verifica se há algum candidato na lista de candidatos
                if len(urna.candidatos) != 0:

                    numero = int(input('Digite o número do Candidato: '))

                    #verificador
                    if urna.verificar_numero(numero):
                        urna.deletar_candidato(numero)
                        print('Candidato deletado com sucesso!')
                        system('pause')

                    else:
                        print('Candidato não existe')
                        system('pause')                    

                else:
                    print('Não existem candidatos cadastrados')
                    system('pause')

            elif opt == MOSTRAR_CANDIDATOS:
                for candidato in urna.candidatos:
                    print(candidato)
                system('pause')

            elif opt == VOLTAR:
                break

            else: #caso ele digite um valor inválido
                print('Opção inválida')
                system('pause')

    elif opt == REALIZAR_ELEICOES:
        while True:
            menu_eleicao()
            opt = int(input('Digite uma opção: '))
            
            if opt == REALIZAR_ELEICAO:   
                print('Eleições iniciadas, em caso de empate, a decisão será no jokempô')
                while True:
                    voto = int(input('Digite o número que deseja votar (-1 para encerrar): '))
                    if voto != -1:
                        if urna.fazer_votacao(voto):
                            print(f'Você votou em {voto}')
                        else:
                            print('Não existe esse candidato, tente novamente')
                    else:
                        print('Eleições Finializadas')
                        system('pause')
                        break

            elif opt == FINALIZAR_ELEICAO:
                resultado = urna.apurar_vencedor(urna)
                if type(resultado) is list:
                    print("Empate entre os seguintes candidatos:") #as vezes ele buga, mostrando apenas o vencedor
                    for candidato in resultado:
                        print(candidato.numero)
                    system('pause')
                else:
                    print(f"O vencedor é: {resultado.nome}!!")
                    system('pause')
                
            elif opt == VOLTAR:
                break

            else: #caso ele digite um valor inválido
                print('Opção inválida')
                system('pause')

    elif opt == SAIR:
        print('Programa encerrado')
        break
    
    else: #caso ele digite um valor inválido
        print('Opção inválida')
        system('pause')

class Candidato:
    def __init__(self, nome, cpf, numero):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.votos = 0

    def __str__(self):
        return f'Candidato {self.nome} de cpf {self.cpf} usa o número {self.numero}\nTeve um total de {self.votos} votos'


class Urna:
    def __init__(self):
        self.candidatos = []
        
    def adicionar_candidato(self, candidato, numero):
        if self.isNumeroRepetido(numero):
            raise CandidatoRepetidoException
        self.candidatos.append(candidato)
        return True
    
    def editar_candidato(self, novo_candidato, numero):
        for candidato in self.candidatos:   
            if candidato.numero == numero:
                indice = self.candidatos.index(candidato)
                self.candidatos[indice] = novo_candidato
                return True
        return False

    def deletar_candidato(self, numero):
        for candidato in self.candidatos:
            if candidato.numero == numero:
                self.candidatos.remove(candidato)

    def fazer_votacao(self, numero):
        for candidato in self.candidatos:
            if candidato.numero == numero:
                candidato.votos += 1
                return candidato
        return False

    def verificar_numero(self, numero):
        for candidato in self.candidatos:
            if candidato.numero == numero:
                return True
        return False

    def apurar_vencedor(self, urna):
        vencedor = self.candidatos[0]
        empatados = []
        candidatos_sorted = sorted(urna.candidatos, key=lambda candidato: candidato.votos, reverse=True)
        for candidato in candidatos_sorted:
            if candidato.votos > vencedor.votos:
                vencedor = candidato
                empatados.clear()
            elif candidato.votos == vencedor.votos:
                empatados.append(candidato)

        if len(empatados) != 0:
            return empatados
        else:
            return vencedor

    def isNumeroRepetido(self, numero):
        for candidato in self.candidatos:
            if candidato.numero == numero:
                return True
        return False

class CandidatoRepetidoException(Exception):
    pass
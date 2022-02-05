"""
Você deve criar uma classe carro que vai possuir dois atributos compostos
por outras duas classes:
1) Motor
2) Direção

O Motor terá a resposabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
    1) Atributo de dados velocidade;
    2) Método acelerar, que deverá incrementar a velocidade de uma unidade
    3) Método frear, que deverá decrementar a velocidade em duas uinidades

A direção terá a responsabilidade de controlar a direção.
Ela oferece os seguintes atributos
    1) Valor de direção com valores possíveis com: Norte, Sul, Leste, Oeste.
    2) Método girar_a_direita
    3) Método girar_a_esquerda
        Direções
            N
        O       L
            S

    Exemplo:
    #testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    #Testando Direção
    >>> direcao = Direcao()
    >>> direcao.rumo
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.rumo
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.rumo
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.rumo
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.rumo
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.rumo
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.rumo
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.rumo
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.rumo
    'Norte'

    >>> carro = Carro()
    >>> carro.calcular_velocidade()
    4
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    5
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    6
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    4
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Leste'
"""

class Motor:
    def __init__(self, ):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        self.velocidade

    def frear(self):
        if self.velocidade <= 0:
            print('carro ja está parado !')
        elif self.velocidade == 1:
            self.velocidade -= 1
        else:
            self.velocidade -= 2


class Direcao:
    def __init__(self):
        self.direcoes = ['Norte','Leste','Sul','Oeste']
        self.rumo = self.direcoes[0]

    def girar_a_direita(self):
        if self.rumo == self.direcoes[0]:
            self.rumo = self.direcoes[1]
        elif self.rumo == self.direcoes[1]:
            self.rumo = self.direcoes[2]
        elif self.rumo == self.direcoes[2]:
            self.rumo = self.direcoes[3]
        else:
            self.rumo = self.direcoes[0]

    def girar_a_esquerda(self):
        if self.rumo == self.direcoes[0]:
            self.rumo = self.direcoes[3]
        elif self.rumo == self.direcoes[3]:
            self.rumo = self.direcoes[2]
        elif self.rumo == self.direcoes[2]:
            self.rumo = self.direcoes[1]
        else:
            self.rumo = self.direcoes[0]


class Carro:
    def __init__(self, motor = Motor(), direcao = Direcao() ):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
         return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
       return self.direcao.rumo


carro = Carro()
print(carro.calcular_direcao())
carro.girar_a_direita()
print(carro.calcular_direcao())
carro.acelerar()
carro.acelerar()
carro.acelerar()
carro.acelerar()
print(carro.calcular_velocidade())
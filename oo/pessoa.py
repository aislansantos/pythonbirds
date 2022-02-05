
class Pessoa: # nome de classe segundo a pep8 usa-se CamelCase
    olhos = 2


    def __init__(self,*filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    # método de classe
    # decorator - são metodos que começam com @, funciona como uma função atrelada a classe Pessoa por isso ela inepende do objeto ->
    # -> não precisando do self
    @staticmethod
    def metodo_statico():
        return 42

    # para criar um metodo de classe usamos o classmethod
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


if __name__ == '__main__':
    augusto = Pessoa(nome ='Augusto')
    aislan = Pessoa(augusto, nome ='Aislan')
    print(Pessoa.cumprimentar(aislan))
    print(id(aislan))
    print(aislan.cumprimentar())
    print(aislan.nome)
    # atributo coplexo
    for filho in aislan.filhos:
        print(filho.nome)
    #atributo dinamico - não é uma pratica ficar criando atributo dinamico, podendo ser usado somente em alguns casos específicos
    aislan.sobrenome = 'Santos'
    del aislan.filhos
    print(aislan.__dict__)
    print(augusto.__dict__)
    print(Pessoa.olhos)
    print(aislan.olhos)
    print(augusto.olhos)
    print(Pessoa.metodo_statico(), aislan.metodo_statico())
    print(Pessoa.nome_e_atributos_de_classe(), aislan.nome_e_atributos_de_classe())
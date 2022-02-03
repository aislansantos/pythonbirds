
class Pessoa: # nome de classe segundo a pep8 usa-se CamelCase
    def __init__(self,*filhos, nome = None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

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
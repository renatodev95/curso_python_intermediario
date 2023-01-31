# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('John', 'Doe')
# p1.nome = 'John'
# p1.sobrenome = 'Doe'

p2 = Pessoa('Sam', 'Martin')
# p2.nome = 'Sam'
# p2.sobrenome = 'Martin'

print(f'{p1.nome} {p1.sobrenome}')
print(f'{p2.nome} {p2.sobrenome}')

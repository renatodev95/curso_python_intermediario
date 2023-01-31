# Métodos em instâncias de classes Python

class Carro:
    def __init__(self, nome, marca):
        self.nome = nome
        self.marca = marca

    def aceletar(self):
        print(f'{self.nome} está acelerando...')

    def frear(self):
        ...


fusca = Carro('Fusca', 'Volkswagen')
celta = Carro('Celta', 'Chevrolet')

print(fusca.nome)
fusca.aceletar()


print(celta.nome)
celta.aceletar()

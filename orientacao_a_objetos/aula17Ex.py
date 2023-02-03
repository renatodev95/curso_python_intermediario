# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

def exibir_dados_carro(car):
    print(f'Carro: {car.nome} \t Motor: {car.motor.nome} \t Fabricante: {car.fabricante.nome}')


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor_new):
        self._motor = motor_new

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fab):
        self._fabricante = fab


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


audi = Carro('Audi A3')
fabricante = Fabricante('AUDI')
motor = Motor('V8')
audi.motor = motor
audi.fabricante = fabricante
exibir_dados_carro(audi)

fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
exibir_dados_carro(fusca)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
exibir_dados_carro(fiat_uno)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
exibir_dados_carro(focus)

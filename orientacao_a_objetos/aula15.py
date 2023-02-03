# Relações entre classes: agregação
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos)

    def total(self):
        return f'R$ {round(sum([produto.preco for produto in self._produtos]), 2)}'

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, new_name):
        self.__nome = new_name

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, new_price):
        self.__preco = new_price


c = Carrinho()
p1 = Produto('Mouse', 567.99)
p2 = Produto('Teclado', 776.99)
p3 = Produto('GPU', 5000.99)
c.inserir_produtos(p1, p2, p3)

c.listar_produtos()
print(c.total())

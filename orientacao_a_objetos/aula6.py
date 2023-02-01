#  __dict__ e vars para atributos de instância


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'Joao', 'idade': 35}
p1 = Pessoa(**dados)

print(p1.__dict__)
print(vars(p1))

# são métodos interessantes para serializar um objeto em JSON, por exemplo

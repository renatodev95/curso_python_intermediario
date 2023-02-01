""" Exercício + if __name__ == '__main__' """

import json

from aula7_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)

    for index, pessoa in enumerate(pessoas):
        p = Pessoa(**pessoas[index])
        print(p.nome, p.idade)

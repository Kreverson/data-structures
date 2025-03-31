import time
import math

def pesquisa_binaria(lista, itemProcurado):
    baixo = 0
    alto = len(lista) - 1
    logTentativas = 0

    while baixo <= alto:
        logTentativas += 1

        meio = math.ceil((baixo + alto) / 2)
        itemLista = lista[meio]

        if itemProcurado == itemLista:
            print_log(logTentativas, len(lista))
            return meio

        if itemProcurado > itemLista:
            baixo = meio + 1
        elif itemProcurado < itemLista:
            alto = meio - 1
        else:
            return None

def pesquisa_simples(lista, itemProcurado):
    index = 0
    logTentativas = 0

    while index <= len(lista) - 1:
        logTentativas += 1
        itemLista = lista[index]

        if itemLista == itemProcurado:
            print_log(logTentativas, len(lista))
            return index
        else:
            index += 1

    return None

def print_log(logTentativas, length):
    print(logTentativas, "tentativas executadas para", length, "elementos")

lista = range(1000)
itemProcurado = 999

print("***** LISTA *****")
print(lista)
print("***** VALOR PROCURADO *****")
print(itemProcurado)


print("***** INICIANDO PESQUISA BINÁRIA *****")
print("Encontrado na posição do array" , pesquisa_binaria(lista, itemProcurado))

print("***** INICIANDO PESQUISA SIMPLES *****")
print("Encontrado na posição do array" , pesquisa_simples(lista, itemProcurado))

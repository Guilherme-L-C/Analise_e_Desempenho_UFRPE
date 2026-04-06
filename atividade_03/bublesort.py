import timeit

lista = []
file = open('numeros.txt', 'r')
for i in file:
    p = i.split()
    for j in p:
        lista.append(int(j))
file.close()

# bublesort
VALOR = 5 # quantidade de vezes que o algoritmo será executado
def bubble_sort(itens): 
    for i in range(len(itens)):
        for j in range(len(itens) -i -1):
            if itens[j] > itens[j + 1]:
                itens[j], itens[j + 1] = itens[j + 1], itens[j]
    return itens

tempo = timeit.timeit(lambda: bubble_sort(lista.copy()), number=VALOR)
media = tempo/VALOR

print(f"BUBLE SORT: {VALOR}x: {media} media de tempo em segundos, lista ordenada: {bubble_sort(lista)}")

with open('arq-ordenado_buble.txt', 'w') as arquivo:   
    for n in lista:
        arquivo.write(str(n) + " ")

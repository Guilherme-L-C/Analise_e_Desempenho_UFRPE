import timeit

lista = []
file = open('numeros.txt', 'r')
for i in file:
    p = i.split()
    for j in p:
        lista.append(int(j))
file.close()


#quicksort
def quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left -1

    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
    arr[1+i], arr[right] = arr[right], arr[i+1]
    return i + 1
    

VALOR = 5 # quantidade de vezes que o algoritmo será executado

tempo = timeit.timeit(lambda: quicksort(lista.copy(), 0, len(lista)-1), number=VALOR)
media = tempo/VALOR

quicksort(lista, 0, len(lista)-1)
print(f"QUICKSORT: {VALOR}x: {media} media de tempo em segundos, lista ordenada: {lista}")

with open('arq-ordenado_quick.txt', 'w') as arquivo:   
    for n in lista:
        arquivo.write(str(n) + " ")

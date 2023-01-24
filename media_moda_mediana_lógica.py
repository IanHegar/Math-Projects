def mediana(lista):
    lista.sort()

    if len(lista) % 2 != 0:
        mediana = (len(lista) // 2)
        return lista[mediana]
    
    else:
        meio = len(lista) // 2
        mediana = (lista[meio] + lista[meio - 1]) / 2
        return mediana


def moda(lista):
    cont = 0
    quantidade = 0
    moda = 0

    for n in lista:
        num = lista.count(n)

        if cont == 0:
            moda = n
            quantidade = num
            cont += 1
        else: 
            if num > quantidade: moda = n
    
    return moda


def media(lista): return sum(lista) / len(lista)
def median(list):
    list.sort()

    if len(list) % 2 != 0:
        median = (len(list) // 2)
        return list[median]
    
    else:
        middle = len(list) // 2
        median = (list[middle] + list[middle - 1]) / 2
        return median


def mode(list):
    cont = 0
    amount = 0
    mode = 0

    for n in list:
        num = list.count(n)

        if cont == 0:
            mode = n
            amount = num
            cont += 1
        else: 
            if num > amount: mode = n
    
    return mode


def mean(list): return sum(list) / len(list)
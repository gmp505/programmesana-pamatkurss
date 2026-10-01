import random

saraksts = [random.randint(1, 100) for _ in range(1000)]


def linear_search(saraksts, mekletais):
    soli = 0

    for i, elements in enumerate(saraksts):
        soli += 1

        if elements == mekletais:
            return i, soli

    return -1, soli

def binary_search(saraksts, mekletais):
    apaksa = 0
    augsa = len(saraksts) - 1
    soli = 0

    while apaksa <= augsa:
        soli += 1
        vidus = (apaksa + augsa) // 2

        if saraksts[vidus] == mekletais:
            return vidus, soli
        elif saraksts[vidus] < mekletais:
            apaksa = vidus + 1
        else:
            augsa = vidus - 1

    return -1, soli


print(len(saraksts))

print(linear_search(saraksts, saraksts[5]))
print(linear_search(saraksts, 999))

saraksts.sort()


print(binary_search(saraksts, saraksts[5]))
print(binary_search(saraksts, 999))
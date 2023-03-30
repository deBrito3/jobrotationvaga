def calc_total(distrib):
    total = 0
    for i in distrib.values():
        total += i
    return total


def represent(distrib, total):
    print(f"Valor total R$ {total}")
    for i in distrib.keys():
        percent = distrib[i] / total * 100
        print(f"{i} - R$ {distrib[i]} - {percent:.2f}%")


distrib = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}

total = calc_total(distrib)
represent(distrib, total)

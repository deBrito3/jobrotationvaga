import json


def average(array):
    days = 0
    total = 0
    for i in array:
        if i["valor"] == 0:
            continue
        days += 1
        total += i["valor"]
    return total / days


def find(array):
    avg = average(array)
    days = 0
    menor = array[0]
    maior = array[0]
    for i in array:
        if i["valor"] == 0:
            continue
        if i["valor"] < menor["valor"]:
            menor = i
        if i["valor"] > maior["valor"]:
            maior = i
        if i["valor"] > avg:
            days += 1

    print(f"O menor valor encontrado desconsiderando finais de semanas e feriados foi de: {menor['valor']} no dia {menor['dia']}.")
    print(f"O maior valor encontrado desconsiderando finais de semanas e feriados foi de: {maior['valor']} no dia {maior['dia']}.")
    print(f"A média mensal foi de: {avg} e o número de dias maior que a média foi de : {days}")


with open("dados.json", "r") as file:
    content = file.read()
    array = json.loads(content)
    find(array)

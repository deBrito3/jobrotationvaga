

def find_fibonacci(number):
    if number == 0:
        return True
    n1 = 0
    n2 = 1
    n3 = 1
    while n3 < number:
        n1 = n2
        n2 = n3
        n3 = n1 + n2

    return n3 == number


number = int(input("Digite o número escolhido:"))

if find_fibonacci(number):
    print(f"O número {number} faz parte da sequência")
else:
    print(f"O número {number} não faz parte da sequência")



def reverse(word):
    for letra in range(len(word) - 1, -1, -1):
        print(word[letra], end="")


word = input("Digite uma palavra:")
reverse(word)

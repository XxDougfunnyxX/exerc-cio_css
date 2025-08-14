frase = input("Quantas vogais tem nessa frase ? ")
vogais ="aeiouAEIOU"
contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print("Quantidade de vogais é: ",contador)
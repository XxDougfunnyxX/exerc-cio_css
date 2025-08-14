numero = int(input("Digite o numero que se deseja determinar o fatorial"))

fatorial =1
for termo in range(1,(numero +1)):
    fatorial *= termo

    print("O fatorial de "+ str(numero)+ "! é:" + str(fatorial))
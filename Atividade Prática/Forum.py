#Tarefa de Pesquisa:Qual sistema o celular usa: IOS ou Android?Todo dia a pesquisa devera recomeçar,mas os valores do dia anterior deverão ser guardados

from datetime import date

# Nome do arquivo onde os votos são guardados
ARQUIVO = "respostas.txt"

# Data de hoje
hoje = date.today().isoformat()

# Faz a pergunta ao usuário
print("Qual sistema seu celular usa?")
print("1 - iOS")
print("2 - Android")

resposta = input("Digite o número da opção: ")

# Define a resposta com base na escolha
if resposta == "1":
    sistema = "iOS"
elif resposta == "2":
    sistema = "Android"
else:
    print("Opção inválida!")
    exit()

# Salva a resposta no arquivo
with open(ARQUIVO, "a") as f:
    f.write(f"{hoje} - {sistema}\n")

print("Resposta registrada com sucesso!")

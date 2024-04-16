#exemplo para se guardar dados dentro de uma variável
quantidade = 20
print (quantidade)
#exemplo de recebimentos de dados pelo usuário
nome = input("Digite seu nome: ")
#utilizando format string, concatenando Texto com varíavel
print (f'O nome digitado foi: {nome}')

#exemplo utilizando  o que foi aprendido acima
nome1 = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
#saída de dados
print(f'Olá {nome1}, você tem {idade} anos')

#---------------------------------------#
#trabalhando com conversão de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

print(nota1 + nota2)

#----------------------------------------#
#Operadores aritméticos
# + soma
# - subtração
# / divisão trazendo casas decimais caso tenha no resultado
# // divisão porém o resultado só traz o número inteiro
# % traz o resto da divisão caso tenha
# * multiplicação
# ** exponênciação

#-----------------------------------------#
#Operadores relacionais
# > maior que
# < menor que
# == igual que
# >= maior ou igual que
# <= menor ou igual que
# != diferente que

comparacao = 10 == 10
print(comparacao)

#------------------------------------------#
#Operadores lógicos [and our not]

logicos = not "Thiago" == "Thiago"
print(logicos) # resultado será o contrário, neste caso será false

#--------------------------------------------#
#Estruturas de decisão
notas1 = int (input("Digite sua primeira nota: "))
notas2 = int (input("Digite sua segunda nota: "))
frequenia_aluno = int(input("Digite sua frequencia: "))

media = (notas1 + notas2) / 2

if media >= 6 and frequenia_aluno >= 75:
    print("Aluno Aprovado!")
else:
    print("Aluno reprovado!")

#--------------------------------------------#
#Laços de repetição

i = 1
while i <= 10:
    print(f'{2} x {i} = {2 * i}')
    i = i + 1

while True:
    nota_aluno = int(input('Digite a nota do aluno: '))
    if nota_aluno >= 0 and nota_aluno <= 10:
        break
    else:
        print("Nota inválida, digite!!")

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#utilizando o step do range
for i in range(1, 11,2):
    print(i)

#fazendo a tabuada utilizando o range
for i in range(1, 11):
    print(f'{2} x {i} = {2 * i}')

# aninhando for
for i in range(1, 6):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')
    print("=======================")

    # Listas
medias_alunos = [2, 4, 5, -3]

#interando com a lista utilizando o for
for i in medias_alunos:
    print(f'O valor da lista atual é: {i}')

#adicionando um valor a lista na última posição
medias_alunos.append(40)
print(medias_alunos)

#Exemplo prático utilizando listas
media_aluno = []

while True:
    nota = int(input('Digite as notas ou -1 para sair: '))
    if nota == -1:
        break
    media_aluno.append(nota) #adicionando a nota na última posição da lista

soma = 0
quantidade = 0
for i in media_aluno:
    soma = soma + i
    quantidade = quantidade + 1

print(soma/quantidade)

#------------------------------#
#DICIONÁRIOS
#          key, value = chave, valor
pessoas = {'nome': 'Pedro', 'idade': 55}
print(pessoas['nome'])

#atribuindo uma chave valor
pessoas['cep'] = '03191111'
print(pessoas)

#--------------------------------#
#FUNÇÕES

#definindo uma função
def calcula_media():
    print('Estou')
    print('Aqui')

#chamando a função
calcula_media()

#funções com passagem de parâmetros

def media(n1, n2):
    print((n1 + n2) / 2)

media(10, 5)
    

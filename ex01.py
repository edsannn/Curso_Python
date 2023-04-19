"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

try:
    entrada = int(input ("Digite um número inteiro: "))
    if entrada % 2 == 0:
            print ("O número digitado é par")
    else:
        print ("O numero digitado é impar")

except ValueError:
    print("Você deve informar um número inteiro!")


hora = int(input("Qual é a hora atual? "))

if hora >= 0 and hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
elif hora > 24:
    print("Horário Inexistente")
else: 
    print("Boa Noite!")

nome = str(input("Qual é o seu nome? "))

if len(nome) <= 4:
    print("Seu nome é curto!")
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")
'''nome = input("Diga seu nome: ")
primeiro_numero = int(input (f"{nome}, diga o primeiro número : "))
segundo_numero = int(input(f"{nome}, diga o segundo número: "))

soma = primeiro_numero + segundo_numero
print(f"A some entre {primeiro_numero} e {segundo_numero} dá {soma}")

operacao = primeiro_numero - segundo_numero
print(f"A subtração entre {primeiro_numero} e {segundo_numero} dá {operacao}")

operacao = primeiro_numero / segundo_numero
print(f"A divisão entre {primeiro_numero} e {segundo_numero} dá {operacao}")

operacao = primeiro_numero * segundo_numero
print(f"A multiplicação entre {primeiro_numero} e {segundo_numero} dá {operacao}")


# variável acumuladora
frase = "O"
print(frase)
frase= frase + " São Paulo"
print(frase)
frase = frase + " foi"
print(frase)
frase = frase + " roubado"
print(frase)
frase = frase + " domingo"


# Booleanas
primeiro_numero = 2
segundo_numero =3
a = primeiro_numero>segundo_numero
print(f"A comparação {primeiro_numero} > {segundo_numero} dá {a}")
a = primeiro_numero>=segundo_numero
print(f"A comparação {primeiro_numero} >= {segundo_numero} dá {a}")
a = primeiro_numero<segundo_numero
print(f"A comparação {primeiro_numero} < {segundo_numero} dá {a}")
a = primeiro_numero<=segundo_numero
print(f"A comparação {primeiro_numero} <= {segundo_numero} dá {a}")
a = primeiro_numero==segundo_numero
print(f"A comparação {primeiro_numero} == {segundo_numero} dá {a}")
a = primeiro_numero!=segundo_numero
print(f"A comparação {primeiro_numero} != {segundo_numero} dá {a}")


a = 2
b = 3
c = 4
d = 5

print(f"A comparação {a} > {b} or {c} > {d}, ou seja, {a>b} or {c>d} dá {a>b or c>d}")
print(f"A comparação {a} < {b} or {c} > {d}, ou seja, {a<b} or {c>d} dá {a>b or c>d}")
print(f"A comparação {a} < {b} or {c} < {d}, ou seja, {a<b} or {c<d} dá {a<b or c>d}")
print(f"A comparação {a} > {b} or {c} < {d}, ou seja, {a>b} or {c<d} dá {a>b or c<d}")

print()

print(f"A comparação {a} > {b} and {c} > {d}, ou seja, {a>b} and {c>d} dá {a>b and c>d}")
print(f"A comparação {a} < {b} and {c} > {d}, ou seja, {a<b} and {c>d} dá {a>b and c>d}")
print(f"A comparação {a} < {b} and {c} < {d}, ou seja, {a<b} and {c<d} dá {a>b and c<d}")
print(f"A comparação {a} > {b} and {c} < {d}, ou seja, {a>b} and {c<d} dá {a<b and c<d}")

idade = int(input("Diga sua idade: "))
if idade < 18:
    print("Você não pode beber !!!")
    print("Que feio !!!")
else:
    print("Pode beber")


idoso = input("Você é idoso ? ")
cadeirante = input("Você é cadeirante ? ")
if idoso == 'sim' or cadeirante == "sim":
    print("Pode estacionar")


letra = input ("Digite uma letra :")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'u':
    print(f"{letra} é uma vogal !")
else:
    print(f"{letra} não é uma vogal !")


letra =input("Diga uma letra: ")
vogal = False
if letra =='a':
    print("Volgal")
    vogal = True
if letra =='e':
    print("Volgal")
    vogal = True
if letra =='i':
    print("Volgal")
    vogal = True
if letra =='o':
    print("Volgal")
    vogal = True
if letra =='u':
    print("Volgal")
    vogal = True
if not vogal:
    print("consoante")


letra =input("Diga uma letra: ")
vogal = False
if letra =='a':
    print("Volgal")
elif letra =='e':
    print("Volgal")
elif letra =='i':
    print("Volgal")
elif letra =='o':
    print("Volgal")
elif letra =='u':
    print("Volgal")
else:
    print("consoante")


salario = int(input("Digite seu salário: "))
if salario < 1903.98:
    aliquota =0
elif salario <= 2826.65:
    aliquota = 7.5/100
elif salario <= 3751.05 :
    aliquota = 22.5/100
elif salario <= 4664.68 :
    aliquota = 27.5/100
elif salario > 4664.68:

desconto = aliquota * salario
print("")


# Exercício1
v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
if v1 == v2:
    print("Não foi possível efetuar o cálculo.")
elif v1 > v2:
    print(f"{v1}")
elif v2 > v1:
    print(f"{v2}")



# Exercício 2
ano = int(input("Digite o ano em que você nasceu: "))
resultado = 2024 - ano
if resultado >= 16:
    print("Você pode votar!!")
else:
    print("não pode votar!!!")


# Exercício 3
senha = int (input("Digite a senha: "))
if senha == 1234:
    print("Senha correta!!")
else:
    print("Senha incorreta")

# Exercício 4
compradas = int(input("Digite a quatidades de maçãs compradas: "))
if compradas < 12:
    resultado = 0.30 * compradas
    print(f"{resultado}")
else:
    resultado = 0.25 * compradas
    print(f"{resultado}")



# Exercício 5

# Exercício 6

altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")
if sexo == 'm':
    ideal = (72.7 * altura) - 58
    print(f"Com {altura} de altura, você deve pesar {ideal}")
elif sexo == 'f':
    ideal = (62.1 * altura) - 44.7
    print(f"Com {altura} de altura, você deve pesar {ideal}")


# Exercício 7 e 8
lados = int(input("Digite a quantidade de lados: "))
medida = int(input("Digite as medidas em cm: "))
if lados < 3 or lados > 5:
    print("Polígono não identificado")
elif lados == 3:
    area = lados * medida
    print(f"A área desse Triângulo é de {area} cm")
elif lados == 4:
    area = lados * medida
    print(f"A área desse Quadrado é de {area} cm")
elif lados == 5:
    area = lados * medida
    print(f"A área desse Pentágono é de {area} cm")


# Exercício 9

# Exercício 10

lado1 = int(input("Digite a medida de um triângulo: "))
lado2 = int(input("Digite outra medida: "))
lado3 = int(input("Digite a última medida: "))
if lado1 == lado2 == lado3:
    print("Este triângulo é Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Este triângulo é Isóscele")
elif lado1 != lado2 != lado3:
    print("Este triângulo é Escaleno")

# Exercício 11
a1 = int(input("Digite um ângulo: "))
a2 = int(input("Digite outro ângulo: "))
a3 = int(input("Digite o último ângulo: "))
soma = a1 + a2 + a3
if soma == 90:
    print(f"{soma}º é um Triângulo Retângulo")
elif soma > 90:
    print(f"{soma}º é um Triângulo Obtusângulo")
else:
    print(f"{soma}º é um Triângulo Acutângulo")
'''
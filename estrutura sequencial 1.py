#Questão 1
def aloMundo():
    print("Alo mundo")

#Questão 2
def mostrar_Numero():
    n1 = int(input("Informe um número: "))
    print(f"O número informado foi {n1}")

#Questão 3
def soma_Numero():
    n1 = int(input("Informe um número: "))
    n2 = int(input("Informe um número: "))
    print(f"A soma de {n1} com {n2} é {n1+n2}")

#Questão 4

def media_notas():
    n1 = int(input("Informe a primeira nota: "))
    n2 = int(input("Informe a segunda nota: "))
    n3 = int(input("Informe a terceira nota: "))
    n4 = int(input("Informe a quarta nota: "))
    media = (n1+n2+n3+n4)/4
    print(f"A média das notas informadas é: {media}")

#Questão 5
def metro_centimetro():
    metro = int(input("Informe o valor do comprimento em metro: "))
    cm = metro*100
    print(f"O comprimentro de metro em centímero é: {cm}")

#Questão 6
def area_Circulo():
    r = int(input("Informe o raio do círculo: "))
    area = 3.14 * (r**2)
    print(f"A área do circulo com o raio {r} é: {area}")

#Questão 7
def dobroQuadrado():
    b = int(input("informe o lado do quadrado: "))
    area = b*b
    print(f"A área do quadrado é: {area}\nO dobro dessa área é {area*2}")
#Questão 8
def ganha_Hora():
    x = float(input("Informe quanto você ganha por hora: "))
    hrs = float(input("Informe as horas trabalhadas este mês: "))
    total = x*hrs
    print(f"O total do salário neste mes é: {total}")
#Questão 9
def farenheit_celsius():
    f = int(input("Insira o valor do farenheit"))
    c = (5*(f-32))/9
    print(f"O valor de º{f} em Graus Celsius é: {c}ª")
#Questão 10
def celsius_farenheit():
    c = float(input("Informe o valor da temperatura em graus celsius: "))
    f = (c*1.8) + 32
    print(f"O grau celsius {c}º em farenheit é: {f}")
#Questão 11
def inteiro_real():
    n1 = int(input("Me informe o número: "))
    n2 = int(input("Me informe outro número: "))
    n3 = float(input("Me informe o valor do terceiro número: "))
    a = (n1*2)*(n2/2)
    b = (n1*3)+(n3)
    c = n3**3
    print(f"A. O produto do dobro do primeiro com metade do segundo: {a}")
    print(f"B. Soma do triplo do primeiro com o terceiro: {b}")
    print(f"C. Terceiro número real elevado ao cubo")
#Questão 12
def peso_ideal():
    h = float(input("Me informe sua altura: "))
    pesoIdeal = (72.7*h) - 58
    print(f"Seu peso ideal é: {pesoIdeal}")
#Questão 13
def peso_ideal_opt():
    sexo = input("Digite 'm' se você for homem ou digite 'f' se você for mulher")
    h = float(input("Me informe sua altura: "))
    idealF = (62.1*h) - 44.7
    idealM = (72.7*h) - 58
    if sexo == 'm':
        print(f"Seu peso ideal é: {idealM}")
    elif sexo == 'f':
        print(f"Seu peso ideal é: {idealF}")
    else:
        print("sexo inválido")
#Questão 14
def joao_Pescador():
    peso = int(input("Informe o peso em quilos: "))
    if peso <= 50:
        print(f"João não teve quilo excedente pois o peso foi de: {peso}")
    elif peso > 50:
        excesso = peso - 50
        multao = excesso*4.00
        print(f"João teve quilo excedente de {excesso} e leva uma multa de {multao}")

#Questão 15
def inss():
    x = float(input("Informe quanto você ganha por hora: "))
    hrs = float(input("Informe as horas trabalhadas este mês: "))
    salario_bruto = x*hrs
    ir = salario_bruto * (11/100)
    inss = salario_bruto * (8/100)
    sindicato = salario_bruto * (5/100)
    salario_liquido = salario_bruto - ir -inss - sindicato
    print(f"+ Salário Bruto : {salario_bruto:.1f}R$")
    print(f"- IR (11%) : {ir:.1f}R$")
    print(f"- INSS (8%) : {inss:.1f}")
    print(f"- Sindicato ( 5%) : {sindicato:.1f}R$")
    print(f"= Salário Liquido : {salario_liquido:.1f}R$")

#Questão 16
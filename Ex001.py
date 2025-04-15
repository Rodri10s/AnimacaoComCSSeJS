salario = float(input("informe o salário: "))
percent = float(input("Informe o aumento em %: "))
novoSal = salario+(salario*0.25)
print("O novo salário é: ",novoSal)

-----------------------------------------------------

n1 = int(input("Informe uma nota: "))
n2 = int(input("Informe uma nota: "))
n3 = int(input("Informe uma nota: "))

media = (n1+n2+n3)/3
print("A média é: ",media)

---------------------------------------------------
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura: "))

print("Nome: {} - Idade: {} - Altura: {}".format(nome,idade,altura))
print(f"Nome: {nome} - Idade: {idade} - Altura: {altura}" )

---------------------------------------------------

n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = (n1+n2)/2

if media >= 7:
    print("Aprovado!")
elif media < 7 and media >+3:
    print("Fará final!")
else:
    print("Reprovado")
#Crie um programa com uma classe Calculadora, que deverá ser usada para implementar as quatro operações aritméticas fundamentais, sob a forma de métodos da classe (adição, subtração, multiplicação e divisão). A classe deverá conter dois atributos chamados primeiroOperando e segundoOperando, que serão usados para armazenar os valores a serem operados, sempre que o objeto de Calculadora for acionado.

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar\n (\n1- +,\n2- -,\n3- *,\n4- /\n):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)

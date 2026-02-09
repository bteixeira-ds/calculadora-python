print("***CALCULADORA***")

num_1 = int(input("Insira o primeiro número: "))
operacao = input("Insira a operação +, -, * ou /: ")
num_2 = int(input("Insira o segundo número: "))

if operacao == "+":
    print(num_1+num_2)
elif operacao == "-":
    print(num_1-num_2)
elif operacao == "*":
    print(num_1*num_2)
elif operacao == "/":
    print(num_1/num_2)
else:
    print("Operação invalida")
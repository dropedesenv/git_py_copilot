#VAMOS SOLICITAR A ENTRADA DE DOIS NUMEROS E DEPOIS REALIZAR A OPERAÇÕE MATEMATICA DE SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO


#SOLICITANDO A ENTRADA DE DOIS NUMEROS


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

#REALIZANDO AS OPERAÇÕES MATEMATICAS

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

#IMPRIMINDO OS RESULTADOS

if operacao == "+":
    print(f"O resultado da soma é: {soma}")
elif operacao == "-":
    print(f"O resultado da subtração é: {subtracao}")
    print(f"O valor absoluto é: {abs(subtracao)}")
elif operacao == "*":
    print(f"O resultado da multiplicação é: {multiplicacao}")
elif operacao == "/":
    print(f"O resultado da divisão é: {divisao}")
else:
    print("Operação inválida")



#FIM DO PROGRAMA

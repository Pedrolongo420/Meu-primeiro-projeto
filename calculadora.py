print ("== CALCULADORA ==")

num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

print("\nEscolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operação = input("digite o numero da operação desejada:")

if operação == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operação == "2":
    resultado = num1 - num2
    print("Resultado", resultado)

elif operação == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operação == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
      print("Erro, não é possivel dividir por zero.")

else:
  print("Operação inválida.")

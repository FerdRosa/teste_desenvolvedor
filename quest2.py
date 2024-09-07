def fibonacci(numero):

  a = 0
  b = 1

  while b < numero:
    aux = b
    b = a + b
    a = aux

  return b == numero

numero = int(input("Digite um número: "))

if fibonacci(numero):
  print(f"{numero} pertence a sequência")
else:
  print(f"{numero} não pertence a sequência")
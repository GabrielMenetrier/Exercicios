notas = [20,30,50,70,90,101]
notaA = ["F","E","D","C","B","A"]

nome = []
notaslista = []

e = 1

while True:
  m = input("Nome do Aluno: ")
  n = int(input("Nota do Aluno: "))
  print("\n")
  if n >100 or n<0:
    print("Invalido")
    temp = "error"
  else:
    for i in range (6):
      if n < notas[i]:
        temp = notaA[i]
        break
  nome.append(m)
  notaslista.append(temp)
  for i in range (e):
    print(nome[i],": ",notaslista[i])
  print("\n")
  e = e+1
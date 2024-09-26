#loop-infinito
while True:
  
  
  try:
      
    nome = input("imforme o nome:") 
    idade =int(input("imforme a idade:"))
    #ternario

    saida = "e maior de idade." if idade >=18 else "menor de idade."
    "saida de dados"

    print(f" {nome}{saida}")

    #verificar se o usuario vai fazer outra verificacao
    continuar = input("deseja continuar? 'sim' para continuar ou outro valor para encerrar.").lower()
    if continuar== "sim":
        continue
    else:
        break
  except Exception as e:
    print(f"nao foi possivel verificar a maioridade.{e}")
  finally:
      print("programa finalizado.")
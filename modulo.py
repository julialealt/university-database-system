
def linha (tam=50):
  return '–' * tam


def cabecalho(txt):
  print(linha())
  print(txt.center(50))
  print(linha())


def menu_principal(lista):
  cont = 1
  for item in lista:
    print('{}- \033[34m{}\033[m'.format(cont, item))
    cont += 1
  print(linha())
  while True:
    opcao = input("Digite uma opção: ")
    opcao = opcao.upper()
    if (opcao != "I" and opcao != "V" and opcao != "R" and opcao != "A" and opcao != "S"):
        print('\n\033[31mERRO: Por favor, digite uma opção válida.\033[m \n')
    else:
      return opcao

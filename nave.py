## Definir as variáveis
combustivel = 110
tripulantes = []

## Definir funções:

def viajar():
    ##aqui vamos gastar combustível!!
    global combustivel ##Avisa a função que vamos modificar uma variável externa
    if(combustivel>=30):
     combustivel = combustivel - 30
     print("A nave viajou")
    else:
       print("Você está sem combustível suficiente, Abasteça!")

def abastecer():
   global combustivel
   combustivel = 110
   print("Tanque cheio!⛽")

def status_nave():
   ## Mostre a quantidade de combustível e os tripulantes
   print("------- STATUS DA NAVE -----------")
   print(f"Temos {combustivel} de combustível")
   print(f"Os tripulantes são:{tripulantes}")
   print("----------------------\n")
   
def registrarTripulantes():
   ##Essa função pergunta o nome do tripulante e adiciona na lista de tripulantes
   novosTripulantes = input("Qual o nome do novo tripulante?:") #Pergunta quem
   tripulantes.append(novosTripulantes) ##Inserimos o fulaninho
   print("Tripulante inserido com sucesso!🚀🧑‍🚀")


## Criar um menu

while True: ##Esse loop roda para sempre!
   print("Bem vindo ao menu interativo da nave. Por favor selecione uma opção:")
   print("\n1- Mostrar status da nave | 2-Viajar | 3- Abastecer | 4- Novo Tripulante | 5- Sair")
   opção = input("Escolha:")
   if(opção == "1"):
      status_nave()
   elif(opção == "2"):
      viajar()
   elif(opção == "3"):
      abastecer() 
   elif(opção == "4"):
      registrarTripulantes()
   elif(opção == "5"):
      print("Viagem encerrada!🛣️")
      break




# status_nave()
# registrarTripulantes()
# status_nave()
   
# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()
from core.engine import Engine, MODOS_VALIDOS
import os

eng = Engine()


while True:
    os.system("cls")
    opcao = input("O que gostaria de fazer? \n Alterar modo \n Opção 2 \n Opção 3 \n \n Resposta: ")

    if opcao == "Alterar modo":
        while True:
            os.system("cls")
            print(f"Status atual: {eng.get_modo()}")
            comando = input("Qual o modo desejado? \n \n Resposta:").strip().lower()

            if comando in MODOS_VALIDOS and eng.get_modo() != comando:
                eng.mudar_modo(comando)
                print(f"Modo alterado para: {eng.get_modo()} \n")

            elif comando in MODOS_VALIDOS and comando == eng.get_modo():
                print("Esse modo já está ativo. \n")

            elif comando in ["voltar", "sair"]:
                break

            else:
                modos_formatados = ", ".join(MODOS_VALIDOS)
                print(f"Modo não reconhecido, modos disponíveis: {modos_formatados}\n")
            
            input("Pressione ENTER para contnuar...")

    else:
        print("Opção anda não desenvolvida\n")
        input("Pressione ENTER para contnuar...")
    
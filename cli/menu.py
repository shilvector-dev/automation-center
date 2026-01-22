import os
from core.engine import Engine
from core.errors import EngineError

ERROR_MESSAGES = {
    EngineError.MODE_ALREADY_ACTIVE: "Esse modo já está ativo. \n",
    EngineError.FILE_NOT_FOUND: "Arquivo não encontrado \n",
    EngineError.OBS_CONECTION_FALED: "Falha ao tentar conectar com o OBS Studio"
}

def start_cli():
    try:
        eng = Engine()
    except RuntimeError:
        print(ERROR_MESSAGES[EngineError.FILE_NOT_FOUND])
        input("Pressione ENTER para sair...")
        return

    while True:
        os.system("cls")
        option = input(
            "O que gostaria de fazer?\n " \
            "1 - Alterar modo \n" \
            "2 - sair \n\n" \
            "Resposta: ").strip().lower()

        if option == "1":
            menu_modes(eng)

        elif option == "2":
            print("Encerrando KhanesIA Automation Center...")
            break

        else:
            print("Opção inválida\n\n")
            input("Pressione ENTER para contnuar...")

def menu_modes(eng):
    while True:
        os.system("cls")
        print(f"Status atual: {eng.get_mode()}")
        command = input("Qual o modo desejado? \n \n Resposta:").strip().lower()

        if command in ["voltar", "sair"]:
            break

        result = eng.set_mode(command)
        
        if result:
            if result == EngineError.INVALID_MODE:
                print(f"Modo não reconhecido, modos disponíveis: {", ".join(eng.get_avaiable_modes())}\n")
            else:
                print(ERROR_MESSAGES.get(result, "Erro desconhecido"))
        else:
            print(f"Modo alterado para: {eng.get_mode()}")
            
        input("Pressione ENTER para continuar...")
    
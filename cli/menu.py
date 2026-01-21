from core.engine import Engine, VALID_MODES
from core.errors import EngineError
import os

ERROR_MESSAGES = {
    EngineError.INVALID_MODE: f"Modo não reconhecido, modos disponíveis: {",".join(VALID_MODES)}\n",
    EngineError.MODE_ALREADY_ACTIVE: "Esse modo já está ativo. \n",
    EngineError.FILE_NOT_FOUND: "Arquivo não encontrado \n",
    EngineError.OBS_CONECTION_FALED: "Falha ao tentar conectar com o OBS Studio"
}

def start_cli():
    eng = Engine()

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
            print("Opção inválida\n")
            input("Pressione ENTER para contnuar...")

def menu_modes(eng):
    while True:
        os.system("cls")
        print(f"Status atual: {eng.get_mode()}")
        command = input("Qual o modo desejado? \n \n Resposta:").strip().lower()
        result = eng.set_mode(command)

        if command in ["voltar", "sair"]:
            break

        elif result:
            print(ERROR_MESSAGES.get(result, "Erro desconhecido"))
        else:
            print(f"Modo alterado para: {eng.get_mode()}")
            
        input("Pressione ENTER para continuar...")
    
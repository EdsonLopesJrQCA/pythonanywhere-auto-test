import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from .core.robot_registry import ROBOTS


def execute(name):
    if name in ROBOTS:
        print(f"Iniciando execução do robô: {name}")
        try:
            ROBOTS[name]()
            print(f"Robô {name} executado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar {name}: {e}")
    else:
        print(f"Robô '{name}' não encontrado.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerenciador de Execução de Robôs RPA")
    parser.add_argument("--robot", type=str, help="Nome do robô a ser executado")

    args = parser.parse_args()

    if args.robot:
        execute(args.robot)
    else:
        print("Nenhum argumento fornecido. Use '--robot <nome>'")

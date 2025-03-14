import argparse
import sys
import os
import logging

# Configurar o logger
log_file = os.path.expanduser("~/pythonanywhere-auto-test/logs/robot_log.log")
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Corrigir caminho do sys.path para evitar problemas de importação
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.robot_registry import ROBOTS  # Ajustado para importar corretamente


def execute(name):
    """Executa um robô com base no nome fornecido."""
    if name in ROBOTS:
        logging.info(f"Iniciando execução do robô: {name}")
        try:
            ROBOTS[name]()
            logging.info(f"Robô {name} executado com sucesso!")
        except Exception as e:
            logging.error(f"Erro ao executar {name}: {e}", exc_info=True)
    else:
        logging.warning(f"Robô '{name}' não encontrado.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gerenciador de Execução de Robôs RPA")
    parser.add_argument("--robot", type=str, help="Nome do robô a ser executado")

    args = parser.parse_args()

    if args.robot:
        execute(args.robot)
    else:
        logging.warning("Nenhum argumento fornecido. Use '--robot <nome>'")

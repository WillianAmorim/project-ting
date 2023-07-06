import os
import sys


def txt_importer(path_file):
    nome_arquivo, extensao = os.path.splitext(path_file)
    if extensao != ".txt":
        print("Formato inválido", file=sys.stderr)
        return []
    try:
        with open(path_file, "r") as file:
            line = file.read().split("\n")
            return line
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

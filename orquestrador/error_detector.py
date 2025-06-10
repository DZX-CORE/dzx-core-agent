import os
import py_compile

def detectar_erros(path_repositorio: str) -> list:
    erros = []
    for root, _, files in os.walk(path_repositorio):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                try:
                    py_compile.compile(full_path, doraise=True)
                except py_compile.PyCompileError as e:
                    erros.append(str(e))
    return erros
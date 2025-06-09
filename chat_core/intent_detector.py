import os
import importlib.util

def carregar_detectores():
    detectores = []
    pasta = os.path.join(os.path.dirname(__file__), "../intent_plugins")  # <-- aqui

    if not os.path.exists(pasta):
        print(f"⚠️ Pasta '{pasta}' não existe.")
        return detectores

    for filename in os.listdir(pasta):
        if filename.endswith(".py"):
            caminho = os.path.join(pasta, filename)
            nome_modulo = filename[:-3]

            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            for nome_classe in dir(modulo):
                cls = getattr(modulo, nome_classe)
                if hasattr(cls, "detectar") and callable(getattr(cls, "detectar")):
                    detectores.append(cls)

    return detectores
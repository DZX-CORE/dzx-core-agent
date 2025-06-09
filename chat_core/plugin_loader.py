import os
import importlib.util

def carregar_plugins():
    plugins = []
    pasta = os.path.join(os.path.dirname(__file__), "../plugins")  # <-- aqui

    if not os.path.exists(pasta):
        print(f"⚠️ Pasta '{pasta}' não existe.")
        return plugins

    for filename in os.listdir(pasta):
        if filename.endswith(".py"):
            caminho = os.path.join(pasta, filename)
            nome_modulo = filename[:-3]

            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            for nome_classe in dir(modulo):
                cls = getattr(modulo, nome_classe)
                if hasattr(cls, "handle_comando") and callable(getattr(cls, "handle_comando")):
                    plugins.append(cls())

    return plugins
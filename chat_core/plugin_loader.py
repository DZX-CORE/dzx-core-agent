import os
import importlib.util

def carregar_plugins():
    plugins = []
    pasta = "plugins"

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

                if isinstance(cls, type) and hasattr(cls, "suporta_intencao") and hasattr(cls, "handle_comando"):
                    instancia = cls()
                    plugins.append(instancia)

    return plugins
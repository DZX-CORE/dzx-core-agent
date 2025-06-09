# chat_core/plugin_loader.py
import os
import importlib.util

def carregar_plugins():
    plugins = []
    pasta = "plugins"
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".py") and not arquivo.startswith("__"):
            caminho = os.path.join(pasta, arquivo)
            nome_modulo = f"plugins.{arquivo[:-3]}"
            try:
                spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
                modulo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(modulo)
                if hasattr(modulo, "handle"):
                    plugins.append(modulo)
            except Exception as e:
                print(f"[!] Erro ao carregar plugin {arquivo}: {e}")
    return plugins

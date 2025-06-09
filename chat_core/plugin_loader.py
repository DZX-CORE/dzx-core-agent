import os
import importlib.util

def carregar_plugins():
    plugins = {}
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

            if hasattr(modulo, "executar") and callable(modulo.executar):
                plugins[nome_modulo] = modulo.executar

    return plugins

def executar_plugin(comando, contexto=None):
    plugins = carregar_plugins()

    if comando in plugins:
        return plugins[comando](contexto or {})
    else:
        return f"❌ Nenhum plugin encontrado para o comando '{comando}'."
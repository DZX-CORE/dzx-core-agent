import os
import importlib.util

base_dir = os.path.dirname(os.path.dirname(__file__))  # raiz do projeto
plugins_dir = os.path.join(base_dir, "plugins")

def carregar_plugins():
    plugins = []
    for filename in os.listdir(plugins_dir):
        if filename.endswith("_plugin.py"):
            module_name = filename[:-3]
            file_path = os.path.join(plugins_dir, filename)
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            plugins.append(module)
    return plugins
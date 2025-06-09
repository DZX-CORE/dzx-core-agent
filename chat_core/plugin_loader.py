import os
import importlib.util

def carregar_plugins():
    plugins = []
    plugins_dir = "plugins"

    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            filepath = os.path.join(plugins_dir, filename)
            module_name = filename[:-3]

            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Plugins precisam ter essas duas funções para serem carregados
            if hasattr(module, "suporta_intencao") and hasattr(module, "handle_comando"):
                plugins.append(module)

    return plugins
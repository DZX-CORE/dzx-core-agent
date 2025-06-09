import os
import importlib.util

def carregar_intent_plugins():
    plugins = []
    intent_dir = "chat_core/intent_plugins"
    if not os.path.exists(intent_dir):
        return plugins
    for filename in os.listdir(intent_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            filepath = os.path.join(intent_dir, filename)
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "detectar_intencao"):
                plugins.append(module)
    return plugins

intent_plugins = carregar_intent_plugins()

def detectar_intencao(mensagem: str) -> dict | None:
    for plugin in intent_plugins:
        try:
            resultado = plugin.detectar_intencao(mensagem)
            if resultado:
                return resultado
        except Exception as e:
            print(f"Erro no plugin de intenção {plugin.__name__}: {e}")
    return None
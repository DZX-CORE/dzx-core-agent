import os
import importlib.util

def carregar_detectores():
    detectores = []
    pasta = "intent_plugins"

    for filename in os.listdir(pasta):
        if filename.endswith(".py") and filename != "__init__.py":
            filepath = os.path.join(pasta, filename)
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "detectar"):
                detectores.append(module)

    return detectores

def detectar_intencao(mensagem: str) -> dict | None:
    for detector in carregar_detectores():
        resultado = detector.detectar(mensagem)
        if resultado:
            return resultado
    return None
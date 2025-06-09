import os
import importlib.util

def carregar_detectores():
    detectores = []
    pasta = "intent_plugins"

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
                if isinstance(cls, type) and hasattr(cls, "detectar") and callable(getattr(cls, "detectar")):
                    detectores.append(cls())

    return detectores

def detectar_intencao(mensagem):
    detectores = carregar_detectores()
    print(f"🔍 Detectores carregados: {[d.__class__.__name__ for d in detectores]}")

    for detector in detectores:
        resultado = detector.detectar(mensagem)
        print(f"➡️ {detector.__class__.__name__} => {resultado}")
        if resultado:
            return resultado
    return None
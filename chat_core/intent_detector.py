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
                # Verifica se é classe e se tem método detectar
                if isinstance(cls, type) and hasattr(cls, "detectar") and callable(getattr(cls, "detectar")):
                    detectores.append(cls())  # instancia aqui

    return detectores

def detectar_intencao(mensagem):
    for detector in carregar_detectores():
        resultado = detector.detectar(mensagem)
        if resultado:
            return resultado
    return None
import os

class ErrorDetector:
    def __init__(self, pasta_projeto):
        self.pasta = pasta_projeto

    def detectar_erro(self):
        # Simulação: procura arquivo de log de erro (exemplo)
        caminho_log = os.path.join(self.pasta, "error.log")
        if os.path.exists(caminho_log):
            with open(caminho_log, "r") as f:
                logs = f.read()
            return logs
        return None

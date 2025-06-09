import time

class CorrectionLoop:
    def __init__(self, github_manager, claude_client, error_detector, pasta_projeto, repo_fullname, branch="main"):
        self.github_manager = github_manager
        self.claude_client = claude_client
        self.error_detector = error_detector
        self.pasta_projeto = pasta_projeto
        self.repo_fullname = repo_fullname
        self.branch = branch
        self.loop_ativo = True

    def executar_loop_correcao(self):
        tentativa = 0
        while self.loop_ativo and tentativa < 5:
            logs = self.error_detector.detectar_erro()
            if not logs:
                print("Nenhum erro detectado. Projeto parece estar OK.")
                break

            print(f"Erro detectado, tentativa {tentativa + 1}:")
            print(logs[:300], "...")  # Print parcial dos logs

            sugestao = self.claude_client.analisar_logs_e_sugerir_correcao(logs, self.pasta_projeto)

            # A aplicação da correção ficaria aqui
            print(f"Sugestão de correção: {sugestao[:300]}...")

            # Para exemplo, simulamos que correção foi aplicada manualmente no repo
            # Em um cenário real, a correção seria aplicada por commit ou PR automático

            print("Aguardando aplicação manual ou automática da correção...")

            time.sleep(10)  # Espera simulada para correção

            tentativa += 1

        if tentativa >= 5:
            print("Número máximo de tentativas de correção atingido.")

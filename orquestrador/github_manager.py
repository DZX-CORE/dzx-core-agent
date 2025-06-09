import os
import subprocess
from git import Repo
from github import Github

class GitHubManager:
    def __init__(self, token):
        self.token = token
        self.github = Github(token)

    def clonar_repositorio(self, url, pasta_destino):
        if os.path.exists(pasta_destino):
            print(f"Pasta {pasta_destino} já existe, removendo...")
            subprocess.run(["rm", "-rf", pasta_destino])
        print(f"Clonando {url} para {pasta_destino}...")
        Repo.clone_from(url, pasta_destino)

    def criar_branch(self, repo_fullname, branch_name):
        repo = self.github.get_repo(repo_fullname)
        source = repo.get_branch(repo.default_branch)
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=source.commit.sha)
        print(f"Branch {branch_name} criada em {repo_fullname}")

    def commit_e_push(self, pasta_local, mensagem, branch="main"):
        repo = Repo(pasta_local)
        repo.git.add("--all")
        repo.index.commit(mensagem)
        origin = repo.remote(name="origin")
        origin.push(branch)
        print(f"Commit e push realizados na branch {branch}")

    def criar_pull_request(self, repo_fullname, branch_name, titulo, descricao):
        repo = self.github.get_repo(repo_fullname)
        pr = repo.create_pull(title=titulo, body=descricao, head=branch_name, base=repo.default_branch)
        print(f"Pull request criado: {pr.html_url}")
        return pr.html_url

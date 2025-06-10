import os
import subprocess
from git import Repo
from github import Github

class GitHubManager:
    def __init__(self, token):
        self.github = Github(token)

    def clone(self, url, folder):
        if os.path.exists(folder):
            subprocess.run(["rm", "-rf", folder])
        print(f"Clonando {url} para {folder}")
        Repo.clone_from(url, folder)

    def create_branch(self, repo_name, branch):
        repo = self.github.get_repo(repo_name)
        default_branch = repo.default_branch
        source = repo.get_branch(default_branch)
        repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)
        return f"Branch {branch} criada."

    def commit_and_push(self, folder, msg, branch="main"):
        repo = Repo(folder)
        repo.git.add("--all")
        repo.index.commit(msg)
        origin = repo.remote(name="origin")
        origin.push(branch)

    def create_pr(self, repo_name, branch):
        repo = self.github.get_repo(repo_name)
        pr = repo.create_pull(title="Correção Automática", body="Sugestões de correção geradas pela IA.",
                              head=branch, base=repo.default_branch)
        return pr.html_url

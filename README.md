# dzx-core-agent - Orquestrador de Correção Automática

## Objetivo

Este projeto implementa um orquestrador simples em Python que:

- Recebe o link do repositório via Telegram
- Clona o repositório localmente
- Detecta erros via arquivos de log
- Envia logs para Claude para sugerir correções
- Aplica (simulado) correções no GitHub
- Faz loop até corrigir ou limite de tentativas

## Como usar

1. Configure as variáveis de ambiente:
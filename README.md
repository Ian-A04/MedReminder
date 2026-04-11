# MediReminder CLI

AUTOR: Ian Alves Calado
Disciplina: Bootcamp II
VERSÃO: 1.0.0

## Visão Geral
O **MediReminder** é uma aplicação de linha de comando (CLI) desenvolvida para auxiliar na organização e adesão a tratamentos medicamentosos. 

### O Problema
Muitas pessoas, especialmente idosos e pacientes com doenças crônicas, enfrentam dificuldades para lembrar os horários corretos de seus medicamentos. O esquecimento ou a confusão de horários pode comprometer a eficácia do tratamento e gerar riscos à saúde.

### A Solução
A aplicação oferece uma interface simples onde o usuário ou cuidador pode:
1. Cadastrar medicamentos e seus respectivos horários.
2. Listar todos os remédios agendados para consulta rápida.
3. Garantir que a rotina de saúde esteja organizada em um ambiente digital minimalista.

## Público-Alvo
- Idosos que buscam autonomia.
- Cuidadores que gerenciam múltiplas medicações.
- Pessoas com rotinas agitadas que precisam de um registro centralizado.

## Tecnologias e Boas Práticas
Para garantir a qualidade profissional exigida, o projeto utiliza:
- **Linguagem:** Python 3.10+
- **Gerenciamento de Dependências:** `requirements.txt`
- **Versionamento Semântico:** Seguindo o padrão `MAJOR.MINOR.PATCH` (v1.0.0).
- **Testes Automatizados:** Implementados com `Pytest` para validar a lógica de cadastro.
- **Análise Estática (Linting):** Configurado com `Ruff` para garantir padrões de código.
- **Integração Contínua (CI):** GitHub Actions configurado para rodar testes e lint a cada commit.

## Como Executar o Projeto

### Pré-requisitos
- Python instalado (versão 3.10 ou superior).
- Git (opcional, para clonar o repositório).

### Passo a passo
1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
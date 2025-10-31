# 💰 Sistema Bancário em Python — Funções, SOLID e Clean Code

Este repositório faz parte do **Desafio da DIO.me**: evolução do Sistema Bancário em Python, agora com **funções**, **boas práticas de código**, **Clean Code** e fundamentação nos princípios **SOLID** para uma arquitetura mais escalável e de fácil manutenção.

---

## 🎯 Objetivo do Projeto

Refatorar o sistema bancário previamente criado, separando as funcionalidades em funções específicas e aplicando:

✅ Modularização  
✅ Código limpo e legível  
✅ Organização por responsabilidade  
✅ Regras de negócio bem definidas  

---

## 🧠 Regras de Negócio

- Depósito **somente valores positivos**
- Limite de **R$ 500,00** por saque
- Máximo de **3 saques por dia**
- Saques não podem **exceder o saldo**
- Extrato deve mostrar **todas as operações e saldo final**

Essas regras simulam cenários reais do sistema financeiro.

---

## 🛠 Tecnologias e Boas Práticas

| Conceito               | Aplicação no Projeto                      |
|------------------------|-------------------------------------------|
| ✅ Python 3            | Linguagem principal                       |
| ✅ Clean Code          | Nomes intuitivos, funções curtas e claras |
| ✅ SOLID               | Separação de responsabilidades por função |
| ✅ Tratamento de erros | Validações no fluxo                       |

---

## 🧩 Arquitetura do Sistema

O sistema foi segmentado em funções:

| Função             | Responsabilidade                  |
|--------------------|-----------------------------------|
| `depositar()`      | Validar e registrar depósitos     |
| `sacar()`          | Aplicar regras e registrar saques |
| `exibir_extrato()` | Mostrar histórico e saldo         |
| `menu()`           | Gerenciar interação com o usuário |

> Em futuras versões, essas funções podem evoluir para classes aplicando **mais profundamente o SOLID**.

---

## 📌 Como executar o projeto

1️⃣ Clone este repositório:
```bash
git clone https://github.com/CUSTcoding/sistema-bancario-python-funcoes.git

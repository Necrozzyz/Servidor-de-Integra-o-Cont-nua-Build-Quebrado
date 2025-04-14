# Explicações dos Erros no Projeto SecureInbox

Este documento descreve os tipos de erro propositalmente incluídos no projeto.

## 📁 src/

### calculadora_bugada.py
Erro de sintaxe: falta de dois pontos `:` na definição da função.

### erro_modulo.py
Importação de módulo que não existe: `ModuleNotFoundError`.

### erro_indentacao.py
Erro de indentação: código fora de bloco `IndentationError`.

### erro_import.py
Importação relativa inválida: `ImportError`.

## 📁 tests/

Cada teste está vinculado a um dos códigos com falha. O Jenkins irá apresentar os erros ao executar estes testes.

---

## Como corrigir?

- Verifique a mensagem de erro no Jenkins.
- Localize o arquivo e corrija o problema.
- Reenvie o commit e veja o build passar!
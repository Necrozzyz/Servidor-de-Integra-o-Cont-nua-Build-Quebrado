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

### erro de ambiente
Pode acontecer quando o agente do jenkins ou não tem o python(no caso deste software) ou o tem instalado na versão errada

### erro_variavel
Acontece quando uma variável de ambiente não está definida

### Erro de instalação de pacote
Se você tenta instalar dependências no build (com pip install) e dá problema.

### Erro de Timeout
Se o seu script demora muito para responder e o Jenkins cancela.

### Erro de permissão de arquivos
Se o Python tenta acessar arquivos que o Jenkins não tem permissão.

## 📁 tests/

Cada teste está vinculado a um dos códigos com falha. O Jenkins irá apresentar os erros ao executar estes testes.

---

## Como corrigir?

- Verifique a mensagem de erro no Jenkins.
- Localize o arquivo e corrija o problema.
- Reenvie o commit e veja o build passar!
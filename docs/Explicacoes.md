1. Erro de sintaxe.................calculadora_bugada.py......................SyntaxError................................Mostra erro no parser
2. Falha em teste..................test_calculadora_bugada.py.................AssertionError.............................Mostra erro de lógica
3. Módulo não encontrado...........Código importando módulo inexistente.......ModuleNotFoundError........................Mostra erro de dependência
4. Importação errada/caminho.......from srcX import xyz.......................ImportError................................Mostra importância da estrutura correta
5. Erro de permissão...............Script .sh sem chmod +x....................Permission denied..........................Mostra erro de execução
6. Erro no requirements.txt........Dependência errada no arquivo..............Could not find a version...................Mostra importância do controle de dependência
7. Branch errada no Git............Jenkinsfile com branch: master.............Couldn't find remote ref master............Mostra erro de configuração Git
8. Erro de indentação Python.......Código com espaçamento quebrado............IndentationError...........................Mostra erro de sintaxe avançada
9. Erro no Jenkinsfile	Pipeline...mal formatado..............................WorkflowScript error.......................Mostra que o Jenkins também falha
10. Erro de path relativo..........from ..src import xyz......................ValueError: attempted relative import......Mostra problemas com estrutura de pacotes
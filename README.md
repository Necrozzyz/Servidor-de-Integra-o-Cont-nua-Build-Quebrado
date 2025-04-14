# Servidor-de-Integra-o-Cont-nua-Build-Quebrado

Este projeto foi desenvolvido com o objetivo de ensinar alunos a identificar e corrigir falhas em pipelines de integração contínua usando Jenkins.

## Estrutura

- `src/`: Contém códigos corretos e com erros propositalmente introduzidos.
- `tests/`: Testes automatizados que passam e que falham para cada caso.
- `Jenkinsfile`: Pipeline CI configurada para rodar testes.
- `EXPLICACOES.md`: Descrição detalhada de cada erro proposital.

## Executando localmente

```bash
pip install -r requirements.txt
pytest
```
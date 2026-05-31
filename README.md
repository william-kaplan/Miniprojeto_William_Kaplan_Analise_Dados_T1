# Miniprojeto - Análise de Dados
**Aluno:** William Roland Kaplan
**Turma:** Análise de Dados T1
**Módulo:** 1 - Semana 07

---

## Como executar

1. Clone o repositório ou baixe o arquivo `main.py`
2. Certifique-se que o arquivo `base_varejo.csv` está na mesma pasta
3. Instale a dependência necessária:
pip install pandas
4. Execute no terminal:
python main.py

---

## Sobre o projeto

Análise de Dados aplicada a uma base de varejo com 830.000 registros.
O script realiza limpeza, transformação e agrupamento dos dados, gerando estatísticas e insights.

---

## Dicionário de Dados

| Coluna | Descrição |
|--------|-----------|
| DATA | Data da compra |
| CO_ID | Identificação do número de compra (nota fiscal) |
| CL_ID | Identificação do cliente |
| CL_GENERO | Sexo informado pelo cliente |
| CL_EC | Estado civil: 1-Casado/União estável, 2-Divorciado, 3-Separado, 4-Solteiro, 5-Viúvo |
| CL_FHL | Número de filhos do cliente |
| CL_SEG | Segmentação econômica (classe A, B ou C) |
| PR_ID | Código do produto (SKU) |
| PR_CAT | Categoria do produto |
| PR_NOME | Nome do produto |

---

## Insights obtidos

1. O gênero feminino foi o que mais comprou, com 382.427 compras (~52% do total).
2. A categoria alimentos dominou as vendas, com grande diferença em relação às demais.
3. A classe econômica B foi a que mais comprou, enquanto a classe A registrou o menor volume.

## Problemas remanescentes

1. Valores `#N/D` encontrados na coluna `PR_CAT`, possivelmente erros de cadastro.
2. Colunas `Unnamed 10-13` completamente vazias, possivelmente reservadas para uso futuro.
3. 96.553 registros duplicados encontrados e removidos.

---

## Reflexão sobre ETL e Qualidade de Dados

ETL é o processo de extração dos dados diretamente da base, seguido do tratamento
(limpeza) e por fim o carregamento para análises corretas. A limpeza dos dados é de
extrema importância para que não se tenha uma visão incorreta dos fatos, evitando
insights errados. Por exemplo, se o valor #N/D da coluna PR_CAT não tivesse sido
tratado, poderia gerar uma interpretação incorreta sobre o que aquele valor representa
na análise de categorias. Da mesma forma, as 96.553 duplicatas removidas poderiam
distorcer os agrupamentos e contagens, alterando os resultados.
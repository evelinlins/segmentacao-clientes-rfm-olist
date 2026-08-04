# Segmentacao de Clientes RFM - E-commerce Olist

**Autor:** Evelin Lins  
**Papel:** Analista de Dados Estrategica  
**Tecnologias:** Python (Pandas, Seaborn, Matplotlib), Jupyter Notebook/Google Colab, Excel  

---

## Visao Geral do Projeto

Este projeto tem como objetivo realizar um processo de **ETL (Extract, Transform, Load)** e **Data Analytics** sobre a base de dados publica do e-commerce Olist para criar uma **Single Customer View**. 

A partir da unificacao de dados transacionais, cadastrais e de pagamentos, foi desenvolvida uma **Segmentacao RFM (Recencia, Frequencia e Monetario)**. A analise transforma dados brutos em inteligencia de negocios prescritiva, permitindo que times de Marketing e CRM tomem decisoes baseadas em ROI e Retencao.

---

## Objetivos Estrategicos

1. **Tratamento & Consolidacao (ETL):** Integrar tabelas transacionais (`orders`, `payments`, `customers`) garantindo integridade e validacao de tipos de dados (`datetime`).
2. **Modelagem RFM:**
   * **Recencia (R):** Dias desde a ultima compra ate a data base.
   * **Frequencia (F):** Quantidade total de ordens concluidas por cliente unico.
   * **Monetario (M):** Valor total investido pelo cliente na plataforma.
3. **Scoring & Clusterizacao:** Categorizacao por quintis (`qcut` e `rank`) para mapeamento de personas do negocio.
4. **Planejamento Prescritivo:** Mapeamento do *Health Score* da base e definicao de reguas de comunicacao para CRM.

---

## Stack Tecnologico & Arquitetura

* **Python 3.x:** Linguagem principal do pipeline de dados.
* **Pandas:** Manipulacao de dados, agrupamentos, juncoes (`merge`), engenharia de atributos e expressoes regulares (Regex).
* **Matplotlib & Seaborn:** Visualizacao de dados e graficos de distribuicao/frequencia para exploracao analitica.
* **OpenPyXL / Excel:** Exportacao do pipeline processado para consumo do time de negocios.

---

## Estrutura do Pipeline & Codigo

O fluxo de codigo esta dividido em 5 etapas principais:

### 1. Carregamento e Auditoria (ETL)
```python
df_orders = pd.read_csv('olist_orders_dataset.csv')
df_payments = pd.read_csv('olist_order_payments_dataset.csv')
df_customers = pd.read_csv('olist_customers_dataset.csv')





<img width="1600" height="880" alt="image" src="https://github.com/user-attachments/assets/fbc043ec-4216-4831-92a1-97b95bf0f00a" />


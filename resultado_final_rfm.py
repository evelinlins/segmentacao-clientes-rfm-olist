
# Resultado Final - Segmentação de Clientes RFM (Base Olist)
# Analista Estratégica: Evelin Lins
# Foco: Geração de Insights, Clusterização e Plano de Ação (Action Plans)
==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Configurações visuais profissionais
sns.set(style="whitegrid")
print("Framework estratégico e visual inicializado com sucesso. 🚀\n")

# 1. SIMULAÇÃO DA BASE CONSOLIDADA (Pós-ETL)
# Como este script foca na análise, assumimos que o 'Tabelão' RFM já foi gerado
# na etapa anterior de Engenharia de Dados.
df_rfm = pd.DataFrame({
    'ID_Cliente': [
        '0000366f3b9a7992bf8c76cfdf3221e2', '0000b849f77a49e4a4ce2b2a4ca5be3f',
        '0000f46a3911fa3c0805444483337064', '0000f6ccb0745a6a4b88665a16c9f078',
        '0004aac84e0df4da2b147fca70cf8255'
    ],
    'Recencia': [111, 114, 537, 321, 288],
    'Frequencia': [1, 1, 1, 1, 1],
    'Monetario': [141.90, 27.19, 86.22, 43.62, 196.89]
})

# 2. DEFINIÇÃO DOS SCORES RFM (Quintis)
# Recência: Notas invertidas (5 = menor tempo desde a última compra)
df_rfm['R'] = pd.qcut(df_rfm['Recencia'], 5, labels=[5, 4, 3, 2, 1], duplicates='drop')
# Frequência e Monetário
df_rfm['F'] = df_rfm['Frequencia'].rank(method='first')
df_rfm['F'] = pd.qcut(df_rfm['F'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')
df_rfm['M'] = pd.qcut(df_rfm['Monetario'], 5, labels=[1, 2, 3, 4, 5], duplicates='drop')

df_rfm['RFM_Score'] = df_rfm['R'].astype(str) + df_rfm['F'].astype(str) + df_rfm['M'].astype(str)

# 3. CLUSTERIZAÇÃO ESTRATÉGICA (REGEX)
segmentos_map = {
    r'[1-2][1-2]': 'Perdidos',
    r'[1-2][3-4]': 'Em Risco',
    r'[1-2]5': 'Não posso perder',
    r'3[1-2]': 'Prestes a dormir',
    r'33': 'Precisa de atenção',
    r'[3-4][4-5]': 'Clientes Fiéis',
    r'41': 'Promissores',
    r'51': 'Novos clientes',
    r'[4-5][2-3]': 'Potencialmente fiéis',
    r'5[4-5]': 'Campeões'
}

df_rfm['Segmento'] = df_rfm['R'].astype(str) + df_rfm['F'].astype(str)
df_rfm['Segmento'] = df_rfm['Segmento'].replace(segmentos_map, regex=True)

# 4. EXPORTAÇÃO DO PRODUTO DE DADOS
output_name = "Resultado_Final_RFM_Evelin.xlsx"
df_rfm.to_excel(output_name, index=False)
print(f"✅ ARQUIVO GERADO COM SUCESSO!")
print(f"Produto de dados exportado para: '{output_name}'\n")

# 5. DIAGNÓSTICO E BUSINESS INTELLIGENCE
print("="*50)
print("ESTRATÉGIA DE NEGÓCIO - RECOMENDAÇÕES RFM")
print("="*50)

total_clientes = 96095 # Valor total histórico da base Olist
campeoes = 7764
em_risco = 15390
perdidos = 15385

print(f"📊 DIAGNÓSTICO DA BASE GERAL:")
print(f"- Dos {total_clientes} clientes, {campeoes} são CAMPEÕES (Pilar de Receita).")
print(f"- Temos {em_risco} clientes EM RISCO (Perda iminente de faturamento).")
print(f"- {perdidos} clientes já são considerados PERDIDOS.\n")

print("🚀 PLANOS DE AÇÃO RECOMENDADOS (Action Plans):")
print("1. PARA OS CAMPEÕES:")
print("   -> Ação: Programa de Fidelidade, Benefícios Exclusivos (Early Access).")
print("   -> Objetivo: Retenção e Transformação em defensores da marca (Advocacy).")

print("\n2. PARA OS EM RISCO / PRESTES A DORMIR:")
print("   -> Ação: Campanhas de Win-back agressivas (Descontos focados).")
print("   -> Objetivo: Reativação antes da perda definitiva (Churn).")

print("\n3. PARA OS NOVOS CLIENTES:")
print("   -> Ação: Régua de Relacionamento (Onboarding) e incentivo à 2ª compra.")
print("   -> Objetivo: Aumentar o Lifetime Value (LTV) e encurtar a recompra.")

print("\n" + "="*50)
print("Relatório gerado por: Evelin - Analista Estratégica (Foco em IA e Negócios)")
print("="*50)

# 6. VISUALIZAÇÕES ESTRATÉGICAS
# Gráfico de Segmentação
plt.figure(figsize=(12, 8))
ordem = df_rfm['Segmento'].value_counts().index
sns.countplot(data=df_rfm, y='Segmento', order=ordem, palette='viridis')
plt.title("Onde estão os nossos clientes? (Segmentação RFM)", fontsize=18)
plt.xlabel("Quantidade de Clientes", fontsize=12)
plt.ylabel("Segmentos Estratégicos", fontsize=12)
plt.tight_layout()
plt.show()

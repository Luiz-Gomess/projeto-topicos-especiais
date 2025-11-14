import pandas as pd

df = pd.read_csv("data/hotel_bookings.csv")
df.drop_duplicates(inplace=True)

df.info()

df["company"].value_counts().to_csv("company.csv")

# 31994 
duplicated = df.duplicated().sum()

df[["babies", "children", "adults"]].describe()

df.describe()

reservas_sem_hospedes = df[(df['adults'] == 0) & (df['babies'] == 0) & (df['children'] == 0)]
reservas_sem_hospedes.to_csv("sem_hospedes.csv")

### Limpeza
## Dataset sem as linhas com 0 hóspedes
df_limpo = df[(df['adults'] > 0) | (df['children'] > 0) | (df['babies'] > 0)].copy()
print(len(df))
print(len(df_limpo))

df_limpo[['country', 'agent', 'company']].isnull().sum()
linhas_nulas = df_limpo[df_limpo["country"].isnull()]

# Preenchendo os valores nulos com o valor '0'
df_limpo['company'] = df_limpo['company'].fillna(0)
df_limpo['agent'] = df_limpo['agent'].fillna(0)

## Identificando valores ausentes na coluna 'country'
df_limpo.info()
df_limpo["country"].isnull().sum()

# Substituindo valores nulos pela moda da coluna
moda_country = df_limpo['country'].mode()[0]
df_limpo['country'] = df_limpo['country'].fillna(moda_country)

## Tratando coluna 'adr' com valores negativos e iguais a 0

adr_negativo = df[df['adr'] < 0]
adr_zero = df[df['adr'] == 0]

# Excluindo linhas com valores menores ou iguais a zero.
df_limpo = df_limpo[(df_limpo['adr']) > 0].copy()
df_limpo.describe()




import itertools
import pandas as pd

df = pd.read_csv('data1.csv')

combinations = itertools.product(
    df['ФИО'],
    df['Город'],
    df['Кредитная карта'][~df['Кредитная карта'].isnull()],
    df['Вклад'][~df['Вклад'].isnull()],
    df['Ипотека'][~df['Ипотека'].isnull()])

res = pd.DataFrame(combinations, columns=df.columns)
res[['Кредитная карта', 'Вклад', 'Ипотека']] = \
    res[['Кредитная карта', 'Вклад', 'Ипотека']].astype('int')
res.loc[:99, :].to_csv('result.csv', index=False)

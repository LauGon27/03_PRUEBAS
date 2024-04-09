import pytest
import src.funciones as fn
import pandas as pd


def test_read():
    df_real = fn.read_csv('/home/lalago/aprendizaje/03_PRUEBAS/03_jobs/test/data/','dummie.csv',',')
    data = {'columna1': [123],
            'columna2': [456]
            }
    df_test = pd.DataFrame(data)
    print(df_test)
    print(df_real)
    sus = df_test.subtract(df_real)
    assert (sus == 0).all().all()

def test_standar_cols():
    list_real=['mia', 'palabra_leer']
    list_out = fn.standar_cols(list_real)
    list_test=['MIA', 'PALABRA_LEER']
    assert list_out == list_test

def test_fill():
    data_test = {'columna1': [None,'b'],
                'columna2': ['4',None]
                }
    df_test = pd.DataFrame(data_test)
    data = {'columna1': ['NI','b'],
            'columna2': ['4','NI']
            }
    df_out = pd.DataFrame(data)
    list_cols = ['columna1','columna2']
    for col_name in list_cols:
        df_test = fn.fill(df_test,col_name,'NI')
    assert df_test.equals(df_out)


def test_strip_whitespace():
    data = {'Name': [' John ', 'Anna ', ' Peter', ' Linda '],
            'Age': [' 25', '30 ', ' 35', '40 ']}
    sample_df = pd.DataFrame(data)
    df_stripped = fn.strip_whitespace(sample_df)
    assert df_stripped['Name'].tolist() == ['John', 'Anna', 'Peter', 'Linda']
    assert df_stripped['Age'].tolist() == ['25', '30', '35', '40']


def test_merge():
    data_1 = {'ID': [1, 2, 3],
            'Name': ['John', 'Anna', 'Peter']}
    df1_in= pd.DataFrame(data_1)
    data_2 = {'ID': [2, 3, 4],
            'Age': [25, 30, 35]}
    df2_in=  pd.DataFrame(data_2)
    df_merged = fn.merge(df1_in, df2_in, 'ID', 'ID', 'inner')
    assert 'Name' in df_merged.columns
    assert 'Age' in df_merged.columns
    assert df_merged.shape == (2, 3)

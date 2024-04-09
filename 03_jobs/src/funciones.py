import pandas as pd
import boto3
from io import StringIO
import os
import src.logger_code  as log

def read_csv(folder_path:str,document_name:str,sep_type:str) -> pd.DataFrame:
    try:
        path_complete =  os.path.join(folder_path, document_name)
        df_read = pd.read_csv(path_complete,sep=sep_type)
        return df_read
    except:
        log.logger.error('Error en la lectura de datos')

def standar_cols(list_names:str) -> list:
    try:
        upper_strings = [element.upper() for element in list_names]
        estandar = [element.replace(" ", "_") for element in upper_strings]
        return  estandar
    except:
        log.logger.error('Error al estandarizar columnas')


def fill(df:pd.DataFrame,col_name:str,val_fill:str) -> pd.DataFrame:
    try:
        df[col_name].fillna(val_fill, inplace=True)
        return df
    except:
        log.logger.error('Error al autorellenar')

def strip_whitespace(df:pd.DataFrame) -> pd.DataFrame:
    try:
        df_strip = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        return df_strip
    except:
        log.logger.error('Error al quitar espacios')

def merge(df_in1:str,df_in2:str,left_key:str,right_key:str,type_merge:str):
    try:
        df_merged = pd.merge(df_in1,df_in2,left_on=left_key,right_on=right_key,how=type_merge)
        return df_merged
    except:
        log.logger.error('Error al realizar el join')


def save_df_to_s3(df, bucket_name, file_key):
    # Convert DataFrame to CSV string
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    # Create an S3 client
    s3_client = boto3.client('s3')
    # Upload CSV string to S3
    s3_client.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=file_key)


'''
def change_column_type(df, columns, new_types):
    for col, new_type in zip(columns, new_types):
        df[col] = df[col].astype(new_type)
'''



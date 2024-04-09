import pandas as pd
import funciones as fn

def main():
    df_read = fn.read_csv('/home/lalago/aprendizaje/03_PRUEBAS/00_data/','Crimes_-_2001_to_Present_20240406.csv')
    logger.info('>>Read')
    df_read.columns = fn.upper(df_read.columns)
    #Teniendo en cuenta que los datos son sensibles parano afectar la veracidad de los datos se decidio crear una
    #nueva categoria NO INFORMATION
    list_cols = ['LOCATION_DESCRIPTION', 'DISTRICT']

    for col_name in list_cols:
        df_read = fn.fill(df_read,col_name,'NI')
    logger.info('>>Fill')
    #Este metodo no se utiliza para otras variables porque son codigos de identificacion numericos,
    #coordenadas o indicadores de posicion razon por la cual no se les hizo el procesamiento anterior
    df_read['DATE'] = pd.to_datetime(df_read['DATE'])
    logger.info('>>Cat')
    crimes_cat = fn.read_csv('/home/lalago/aprendizaje/03_PRUEBAS/00_data/','crime_categories.csv')
    crimes_cat = fn.strip_whitespace(crimes_cat)
    crimes_cat.columns = ['CODE', 'CRIME_DESCRIPTION']
    logger.info('>>Merge')
    merge_df= fn.merge(df_read,crimes_cat,'FBI_CODE','CODE','left')
    logger.info('>>End')
    merge_df.to_csv('/home/lalago/aprendizaje/03_PRUEBAS/00_data/df_crimes.csv',sep =',')
    logger.info('>>Save')

    # Specify S3 bucket name and file key
    #bucket_name = 'your-bucket-name'
    #file_key = 'path/to/your/file.csv'

    # Save DataFrame to S3
    #fn.save_df_to_s3(df, bucket_name, file_key)


if __name__=='__main__':
    main()

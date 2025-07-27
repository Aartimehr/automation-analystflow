import pandas as pd
import mysql.connector
import os
excel_files = [
    ('newdata.xlsx' ,'newdata')
    ]
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nikku1234@",
    database="databaseforprac"
)
cursor=conn.cursor()
folder_path="C:/Users/mehra/Downloads/excel folder"
def get_sql_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'INT'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    else:
        return 'TEXT'
for excel_file, table_name in excel_files:
    file_path = os.path.join(folder_path, excel_file)
    
    df = pd.read_excel(file_path)
    
    df = df.where(pd.notnull(df), None)

    print(f"Processing {excel_file}")
    print(f"NaN values before replacement:\n{df.isnull().sum()}\n")

    df.columns = [col.replace(' ', '_').replace('-', '_').replace('.', '_') for col in df.columns]

    columns = ', '.join([f'`{col}` {get_sql_type(df[col].dtype)}' for col in df.columns])
    create_table_query = f'CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})'
    cursor.execute(create_table_query)

    for _, row in df.iterrows():
        values = tuple(None if pd.isna(x) else x for x in row)
        sql = f"INSERT INTO `{table_name}` ({', '.join(['`' + col + '`' for col in df.columns])}) VALUES ({', '.join(['%s'] * len(row))})"
        cursor.execute(sql, values)
    conn.commit()

conn.close()

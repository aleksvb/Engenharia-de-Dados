import boto3
import pandas as pd

#Criar um cliente para interagir com o AWS S3
s3_client = boto3.client('s3')

#s3_client.download_file('','')

s3_client.upload_file('microdados_enem_2019.csv', 'datalake-aleksandro-256541563535', 'data/microdados_enem_2019.csv')



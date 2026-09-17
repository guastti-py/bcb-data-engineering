import os

import boto3
from dotenv import load_dotenv

load_dotenv()

def enviar_para_s3(caminho_local, chave_s3):
    bucket = os.getenv("S3_BUCKET")
    
    if not bucket:
        raise ValueError("A variável S3_BUCKET não foi configurada.")
    
    s3 = boto3.client("s3")
    
    s3.upload_file(
        caminho_local,
        bucket,
        chave_s3
    )
    
    print(f"Arquivo enviado para o S3: s3://{bucket}/{chave_s3}")
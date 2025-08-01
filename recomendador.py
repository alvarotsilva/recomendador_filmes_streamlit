from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from datetime import datetime

# Conexão Azure
connect_str = "SUA CHAVE DO AZURE"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def carregar_dados_azure(container_name, blob_name):
    try:
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_data = blob_client.download_blob().readall().decode('utf-8')
        return pd.read_csv(StringIO(blob_data))
    except Exception as e:
        print(f"Erro ao carregar {blob_name}: {e}")
        return None

def gerar_recomendacoes(df, plataforma, usuario_generos, usuario_assinaturas, n=10):
    if plataforma not in usuario_assinaturas:
        return pd.DataFrame()
    
    df['conteudo'] = df[['listed_in', 'description', 'cast', 'director']].fillna('').agg(' '.join, axis=1)
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['conteudo'])
    usuario_vector = tfidf.transform([usuario_generos])
    sim_scores = cosine_similarity(usuario_vector, tfidf_matrix).flatten()
    
    hoje = datetime.today().year
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').fillna(0).astype(int)
    df['tempo_pop'] = np.exp(-0.1 * (hoje - df['release_year']))
    
    df['score'] = sim_scores * 0.6 + df['tempo_pop'] * 0.4
    return df.sort_values('score', ascending=False).head(n)
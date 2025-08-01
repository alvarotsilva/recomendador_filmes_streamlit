#Auto: Álvaro Tavares - 01/08/2025
#pip install -r requirements.txt
#streamlit run app.py

import streamlit as st
from recomendador import carregar_dados_azure, gerar_recomendacoes

st.set_page_config(page_title="Recomendador de Filmes", layout="wide")
st.title("🎬 Recomendador Híbrido de Filmes por Plataforma")

usuario_generos = st.text_input("Digite seus gêneros, elenco ou temas preferidos:", "comedy drama")
usuario_assinaturas = st.multiselect("Quais plataformas você assina?", ["Netflix", "Amazon Prime", "Disney+"], default=["Netflix"])

containers = {
    "Netflix": ("netflix", "netflix_titles.csv"),
    "Amazon Prime": ("amazon", "amazon_prime_titles.csv"),
    "Disney+": ("disney", "disney_plus_titles.csv")
}

for nome, (container, arquivo) in containers.items():
    with st.expander(f"{nome} 📺", expanded=True):
        df = carregar_dados_azure(container, arquivo)
        if df is not None:
            recs = gerar_recomendacoes(df.copy(), nome, usuario_generos, usuario_assinaturas)
            if not recs.empty:
                st.dataframe(recs[['title', 'release_year', 'listed_in', 'score']])
            else:
                st.warning("Nenhuma recomendação disponível para esta plataforma.")
        else:
            st.error("Erro ao carregar dados.")
# 🎬 Recomendador Híbrido de Filmes por Plataforma

Este projeto é uma aplicação em Python + Streamlit que recomenda filmes e séries de forma personalizada com base em três dimensões:

1. **Conteúdo textual** (gêneros, sinopse, elenco e direção)
2. **Popularidade recente** com decaimento temporal
3. **Disponibilidade na plataforma** (apenas títulos das plataformas assinadas pelo usuário)

---

## 🚀 Como rodar

### 1. Clonar o repositório ou extrair o `.zip`
```bash
unzip recomendador_filmes_streamlit.zip
cd recomendador_filmes_streamlit
```

### 2. Instalar dependências (recomenda-se usar virtualenv)
```bash
pip install -r requirements.txt
```

### 3. Rodar a aplicação
```bash
streamlit run app.py
```

---

## 🧠 Tecnologias utilizadas

- Python
- Streamlit (para a interface)
- Azure Blob Storage (armazenamento dos dados)
- Pandas
- Scikit-learn (TF-IDF + Cosseno)
- NumPy

---

## 🔐 Conexão com Azure

A aplicação já está configurada para se conectar ao seguinte endpoint:

```
Conta: meusdatalakecsvs
Containers: 
  - container-netflix/netflix_titles.csv
  - container-prime/amazon_prime_titles.csv
  - container-disney/disney_plus_titles.csv
```

A connection string está embutida no arquivo `recomendador.py`.

> ⚠️ **Atenção:** nunca exponha a connection string real em ambientes públicos.

---

## 📊 Exibição

- Interface com **3 abas**:
  - Netflix
  - Amazon Prime
  - Disney+
- Atualização em tempo real conforme o usuário digita seus interesses
- Top-10 recomendações para cada plataforma com base no score híbrido

---

## 📁 Estrutura do projeto

```
📂 recomendador_filmes_streamlit
├── app.py                # Interface Streamlit
├── recomendador.py       # Lógica de recomendação + acesso ao Azure
├── requirements.txt      # Dependências
└── README.md             # Documentação
```

---

## 📧 Autor: 
Desenvolvido por Álvaro Tavares - 01/08/2025.  
Para sugestões ou melhorias, entre em contato!

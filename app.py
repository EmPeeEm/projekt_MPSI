import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from sklearn.manifold import TSNE
from sklearn.decomposition import TruncatedSVD
import sys
import os

# Dodanie głównego folderu do ścieżek, aby Python widział folder 'src'
sys.path.append(os.path.abspath('.'))
from src.kmeans import KMeans
from src.utils import get_top_words

# Konfiguracja strony
st.set_page_config(page_title="Wizualizacja NLP", layout="wide")

# --- CACHOWANIE DANYCH I OBLICZEŃ ---
@st.cache_data
def load_data():
    """Wczytuje preprocesowane dane z pliku joblib."""
    return joblib.load('data/tfidf_data.joblib')

@st.cache_data
def compute_tsne(_tfidf_matrix):
    """Wstępnie redukuje wymiary przez SVD, a następnie oblicza t-SNE."""
    # 1. Wstępna redukcja z tysięcy do 50 wymiarów (pomija szum)
    svd = TruncatedSVD(n_components=50, random_state=42)
    tfidf_reduced = svd.fit_transform(_tfidf_matrix)
    
    # 2. Właściwa redukcja t-SNE do 2 wymiarów
    tsne = TSNE(n_components=2, perplexity=30, random_state=42)
    return tsne.fit_transform(tfidf_reduced)

# --- GŁÓWNY INTERFEJS ---
st.title("Wizualizacja Modelowania Tematów w NLP 🧠")
st.markdown("Interaktywny dashboard do analizy klastrów zbioru 20 Newsgroups z wykorzystaniem własnej implementacji algorytmu K-means.")

# Wczytanie danych
try:
    data = load_data()
    documents = data['documents']
    tfidf_matrix = data['tfidf_matrix']
    vectorizer = data['vectorizer']
except FileNotFoundError:
    st.error("Brak pliku `data/tfidf_data.joblib`. Uruchom najpierw notatnik z preprocessingiem i upewnij się, że dane zostały zapisane!")
    st.stop()

# --- PANEL BOCZNY (USTAWIENIA) ---
st.sidebar.header("Parametry modelu")
k_clusters = st.sidebar.slider("Wybierz liczbę tematów (k):", min_value=2, max_value=21, value=4)

# --- OBLICZENIA ---
with st.spinner('Trwa redukcja wymiarów t-SNE (to może chwilę potrwać za pierwszym razem)...'):
    tsne_results = compute_tsne(tfidf_matrix)

with st.spinner(f'Trenowanie modelu K-means dla k={k_clusters}...'):
    # Używamy Waszego własnego modelu z src/kmeans.py
    model = KMeans(n_clusters=k_clusters, init='k-means++', random_state=42)
    model.fit(tfidf_matrix)

# Przygotowanie ramki danych do wykresu
df = pd.DataFrame({
    'x': tsne_results[:, 0],
    'y': tsne_results[:, 1],
    'Klaster': [f"Klaster {label}" for label in model.labels_],
    'Tekst': [doc[:200] + "..." for doc in documents]  # Pierwsze 200 znaków dokumentu do podglądu
})

# --- WIZUALIZACJA ---
st.subheader("Interaktywna mapa klastrów (t-SNE)")

# Tworzenie interaktywnego wykresu punktowego
fig = px.scatter(
    df, x='x', y='y', color='Klaster',
    hover_data={'Tekst': True, 'x': False, 'y': False, 'Klaster': False},
    color_discrete_sequence=px.colors.qualitative.Safe
)
fig.update_traces(marker=dict(size=7, opacity=0.8, line=dict(width=1, color='DarkSlateGrey')))
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.update_layout(
    width=800,
    height=600
)
st.plotly_chart(fig, use_container_width=False)

# --- SŁOWA KLUCZOWE ---
st.subheader("Najważniejsze słowa dla wyznaczonych tematów")
# Używamy Waszej funkcji z src/utils.py
top_words_dict = get_top_words(vectorizer, model.cluster_centers_, n_words=10)

# Wyświetlanie słów w estetycznych kolumnach (po 3 w rzędzie)
cols = st.columns(3)
for i, (cluster_id, words) in enumerate(top_words_dict.items()):
    with cols[i % 3]:
        st.markdown(f"**{cluster_id}**")
        st.info(", ".join(words))
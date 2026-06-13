# 📚 NLP Topic Modeling - Grupowanie dokumentów (20 Newsgroups)

Projekt realizowany w ramach przedmiotu **Metody Programowania i Systemy Inteligentne (MPSI)**. Głównym celem projektu jest automatyczne grupowanie (klasteryzacja) dokumentów tekstowych według tematyki przy użyciu metod NLP (Natural Language Processing) oraz algorytmów uczenia maszynowego bez nadzoru.

---

## 🎯 Cele projektu

- 🧹 **Preprocessing tekstu**: Oczyszczenie danych tekstowych (tokenizacja, usuwanie stop words, znaków interpunkcyjnych, lematyzacja).
- 📐 **Reprezentacja wektorowa**: Przekształcenie tekstów na wektory liczbowe przy użyciu macierzy **TF-IDF** (Term Frequency - Inverse Document Frequency).
- 🤖 **Klasteryzacja**: Zastosowanie algorytmu **k-means** (k-średnich) do pogrupowania artykułów na spójne tematycznie klastry.
- 🔍 **Interpretacja klastrów**: Identyfikacja słów kluczowych najlepiej opisujących poszczególne grupy (najważniejsze cechy o najwyższych wartościach centrowych).
- 📈 **Analiza hiperparametrów**: Zbadanie wpływu liczby klastrów ($k$) na jakość podziału (np. przy użyciu metody łokcia lub współczynnika sylwetki).
- 🗺️ **Wizualizacja**: Redukcja wymiarowości przestrzeni cech metodą **t-SNE** (t-Distributed Stochastic Neighbor Embedding) i prezentacja klastrów na wykresie 2D.

---

## 🛠️ Użyte technologie

- **Python 3.10+** — główny język programowania
- **scikit-learn** — preprocessing (TF-IDF), klasteryzacja (k-means) oraz redukcja wymiarowości (t-SNE)
- **NLTK / Spacy** — zaawansowana analiza lingwistyczna (tokenizacja, lematyzacja)
- **pandas & NumPy** — manipulacja danymi i operacje macierzowe
- **matplotlib & seaborn** — generowanie wykresów i wizualizacji
- **Jupyter Notebook** — środowisko eksperymentalne i prezentacja wyników

---

## 📁 Struktura katalogów

Poniższe drzewo przedstawia strukturę repozytorium projektu:

```text
.
├── data/                               # Zbiór danych 20 Newsgroups (ignorowany przez Git)
├── notebooks/                          # Jupyter Notebooks z eksperymentami
│   ├── 01_preprocessing_i_tfidf.ipynb  # Pipeline czyszczenia danych i ekstrakcji cech
│   └── 02_kmeans_i_tsne.ipynb         # Modelowanie k-means oraz wizualizacja t-SNE
├── src/                                # Moduły z kodem źródłowym Python
│   ├── __init__.py                     # Inicjalizacja pakietu
│   ├── text_prep.py                    # Funkcje oczyszczania i preprocessingu tekstu
│   └── utils.py                        # Funkcje pomocnicze (metryki, wykresy)
├── .gitignore                          # Ignorowane pliki (data/, .venv/, itp.)
├── INSTRUKCJA.md                       # Przewodnik krok po kroku po uruchomieniu lokalnym
├── PLAN_PRACY.md                       # Podział zadań i harmonogram projektu
├── README.md                           # Główny opis projektu (ten plik)
└── requirements.txt                    # Lista wymaganych bibliotek Python
```

---

## 🚀 Więcej informacji

Aby dowiedzieć się więcej o szczegółach projektu, zapoznaj się z poniższymi dokumentami:

- 📋 Szczegółowy podział ról oraz harmonogram prac znajdziesz w pliku [PLAN_PRACY.md](PLAN_PRACY.md).
- 🛠️ Instrukcję instalacji środowiska i uruchomienia notebooków znajdziesz w pliku [INSTRUKCJA.md](INSTRUKCJA.md).

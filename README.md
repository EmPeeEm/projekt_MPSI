# 📚 NLP Topic Modeling - Grupowanie dokumentów (20 Newsgroups)

Projekt realizowany w ramach przedmiotu **Metody Programowania i Systemy Inteligentne (MPSI)**. Głównym celem projektu jest automatyczne grupowanie (klasteryzacja) dokumentów tekstowych według tematyki przy użyciu metod NLP (Natural Language Processing) oraz samodzielnie zaimplementowanych algorytmów uczenia maszynowego bez nadzoru.

---

## 🎯 Cele i wymagania projektu

Zgodnie z wymaganiami przedmiotowymi, projekt obejmuje:
- 💻 **Samodzielna implementacja algorytmów**: Własna implementacja algorytmu **k-means (k-średnich)** od podstaw w języku Python (przy użyciu biblioteki NumPy) w celu głębszego zrozumienia jego mechaniki.
- 🧹 **Preprocessing tekstu**: Oczyszczenie danych tekstowych (tokenizacja, usuwanie stop words, znaków interpunkcyjnych, lematyzacja).
- 📐 **Reprezentacja wektorowa**: Przekształcenie tekstów na wektory liczbowe przy użyciu macierzy **TF-IDF** (Term Frequency - Inverse Document Frequency).
- 🧪 **Eksperymenty i analiza klastrów**:
  - Identyfikacja słów najlepiej opisujących klastry (Top Words na bazie centroidów).
  - Badanie wpływu liczby klastrów ($k$) na jakość podziału (porównanie wyników dla różnych wartości $k$).
- 🗺️ **Wizualizacja t-SNE**: Redukcja wymiarowości cech metodą t-SNE i wizualizacja podziału w 2D.
- 💻 **Aplikacja interaktywna**: Stworzenie interaktywnego panelu w **Streamlit** do prezentacji wyników klasteryzacji na żywo.
- 📑 **Raport w Jupyter Notebook**: Szczegółowe udokumentowanie eksperymentów, interpretacji klastrów oraz wniosków.
- ⚠️ **Analiza ograniczeń**: Krytyczne omówienie słabych stron zastosowanych metod (np. ograniczenia TF-IDF, wrażliwość k-means na inicjalizację i dobór $k$, złożoność obliczeniowa t-SNE) oraz napotkanych problemów.

---

## 🛠️ Użyte technologie

- **Python 3.10+** — główny język programowania
- **NumPy** — niskopoziomowa samodzielna implementacja k-means i operacje macierzowe
- **scikit-learn** — preprocessing (TF-IDF), referencyjna implementacja k-means (do porównań) oraz t-SNE
- **pandas** — strukturyzacja i analiza danych tekstowych
- **matplotlib** — generowanie statycznych wykresów i analiz
- **Streamlit** — interaktywna aplikacja webowa do wizualizacji klastrów i dokumentów w czasie rzeczywistym
- **Jupyter Notebook** — środowisko badawcze i raport końcowy

---

## 📁 Struktura katalogów

```text
.
├── data/                               # Zbiór danych 20 Newsgroups (ignorowany przez Git)
├── notebooks/                          # Jupyter Notebooks z eksperymentami i raportami
│   ├── 01_preprocessing_i_tfidf.ipynb  # Przygotowanie danych i wektoryzacja
│   └── 02_kmeans_i_tsne.ipynb         # Samodzielny k-means, analiza k, t-SNE i wnioski
├── src/                                # Kod źródłowy projektu
│   ├── __init__.py                     # Inicjalizacja pakietu
│   ├── text_prep.py                    # Pipeline preprocessingu tekstu
│   ├── kmeans.py                       # Samodzielna implementacja algorytmu k-means
│   └── utils.py                        # Metryki, ładowanie danych i funkcje rysujące
├── app.py                              # Interaktywna aplikacja Streamlit
├── .gitignore                          # Ignorowane pliki (.venv/, data/, itp.)
├── INSTRUKCJA.md                       # Instrukcja instalacji i uruchomienia lokalnego
├── PLAN_PRACY.md                       # Harmonogram, kamienie milowe i podział zadań
├── README.md                           # Główny opis projektu (ten plik)
└── requirements.txt                    # Zależności projektu
```

---

## 🚀 Więcej informacji

Aby dowiedzieć się więcej o szczegółach projektu, zapoznaj się z poniższymi dokumentami:

- 📋 Szczegółowy podział ról oraz roadmapę realizacji celów znajdziesz w pliku [PLAN_PRACY.md](PLAN_PRACY.md).
- 🛠️ Instrukcję instalacji bibliotek oraz uruchomienia aplikacji Streamlit i Jupyter znajdziesz w pliku [INSTRUKCJA.md](INSTRUKCJA.md).

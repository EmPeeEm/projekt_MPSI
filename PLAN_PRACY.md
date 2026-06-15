# 📋 Plan Pracy i Podział Ról — Projekt MPSI

Niniejszy dokument opisuje podział odpowiedzialności w dwuosobowym zespole projektowym oraz przedstawia szczegółowy harmonogram (roadmapę) realizacji projektu modelowania tematów w NLP, z uwzględnieniem wymogu samodzielnej implementacji algorytmu klasteryzacji.

---

## 👥 Podział ról w zespole

### 👤 Osoba 1: Data, Preprocessing & Interpretability
Odpowiada za potok przetwarzania danych tekstowych, ich reprezentację wektorową oraz semantyczną interpretację i ewaluację klastrów.

- ⚙️ **Przygotowanie potoku danych (Data Pipeline)**:
  - Implementacja czyszczenia i preprocessingu w module [text_prep.py](src/text_prep.py) (tokenizacja, lematyzacja, filtracja stop words).
- 📐 **Reprezentacja wektorowa**:
  - Konfiguracja i optymalizacja transformacji **TF-IDF**.
- 💬 **Interpretacja klastrów i ewaluacja**:
  - Implementacja algorytmu wyciągania najważniejszych słów (Top Words) dla każdego z klastrów na podstawie centroidów.
  - Analiza i ocena spójności semantycznej tematów.
- 📑 **Raportowanie**:
  - Przygotowanie struktury raportu w notebookach i krytyczne omówienie ograniczeń reprezentacji bag-of-words / TF-IDF.
  - Prezentacja pierwszej części projektu (dane, preprocessing, TF-IDF).

---

### 👤 Osoba 2: Custom Modeling, Visualization & UI
Odpowiada za samodzielną implementację algorytmu klasteryzacji, analizę numeryczną klastrów, redukcję wymiarów oraz interaktywny dashboard.

- 🤖 **Samodzielna implementacja algorytmu**:
  - Zakodowanie od podstaw algorytmu **k-means (k-średnich)** przy użyciu NumPy/Python w osobnym module `src/kmeans.py`.
  - Zaimplementowanie mechanizmów inicjalizacji (losowa oraz opcjonalnie k-means++), przypisywania punktów do centroidów i ich aktualizacji.
- 📈 **Eksperymenty i analiza hiperparametrów**:
  - Badanie wpływu liczby klastrów $k$ (metoda łokcia, analiza bezwładności).
  - Porównanie własnej implementacji z referencyjnym modelem z `scikit-learn` pod kątem czasu wykonania i zbieżności.
- 🗺️ **Wizualizacja t-SNE & Streamlit**:
  - Redukcja wymiarowości macierzy TF-IDF do 2D za pomocą t-SNE.
  - Stworzenie interaktywnej aplikacji w **Streamlit** ([app.py](app.py)) do wizualizacji klastrów na żywo.
- 📑 **Raportowanie**:
  - Przygotowanie wykresów do notebooka raportowego oraz krytyczne omówienie ograniczeń algorytmu k-means (czułość na inicjalizację, złożoność obliczeniowa t-SNE).
  - Prezentacja drugiej części projektu (samodzielny model, t-SNE, dashboard Streamlit i wnioski).

---

## 🗺️ Roadmapa Projektu (5 Etapów)

Poniższa lista kontrolna określa kroki niezbędne do ukończenia projektu:

- [x] **Etap 1: Inicjalizacja projektu i strukturyzacja**
  - Stworzenie repozytorium Git i powiązanie z submodułami.
  - Przygotowanie struktury katalogów i plików dokumentacyjnych.
  - Stworzenie pliku `requirements.txt` z bazowymi bibliotekami oraz Streamlitem.
- [x] **Etap 2: Pipeline danych, TF-IDF i szkielet algorytmu (Osoba 1 & Osoba 2)**
  - Opracowanie modułu preprocessingu [text_prep.py](src/text_prep.py) (Osoba 1).
  - Przygotowanie wstępnej wersji wektoryzatora TF-IDF w notebooku [01_preprocessing_i_tfidf.ipynb](notebooks/01_preprocessing_i_tfidf.ipynb) (Osoba 1).
  - Napisanie szkieletu własnego algorytmu k-means w `src/kmeans.py` przy użyciu NumPy (Osoba 2).
- [x] **Etap 3: Testy k-means, analiza $k$ i interpretacja tematów**
  - Uruchomienie własnej implementacji k-means na danych wejściowych (Osoba 2).
  - Przeprowadzenie eksperymentów z różnymi wartościami $k$ (metoda łokcia) (Osoba 2).
  - Ekstrakcja słów kluczowych dla każdego klastra i nadanie im interpretacji tematycznej (Osoba 1).
  - Porównanie metryk i zbieżności z wersją ze `scikit-learn` (Wspólnie).
- [x] **Etap 4: Wizualizacja t-SNE i budowa aplikacji Streamlit**
  - Wygenerowanie rzutowania t-SNE w notebooku [02_kmeans_i_tsne.ipynb](notebooks/02_kmeans_i_tsne.ipynb) w celu oceny rozdzielności klastrów (Osoba 2).
  - Stworzenie aplikacji [app.py](app.py) w Streamlit do interaktywnego przeglądania dokumentów w klastrach oraz dynamicznej prezentacji wykresów t-SNE (Osoba 2).
- [/] **Etap 5: Przygotowanie raportu i prezentacji końcowej**
  - Opracowanie sekcji o ograniczeniach algorytmów (np. problem lokalnych minimów w k-means, brak informacji o kolejności słów w TF-IDF, niestabilność t-SNE) oraz napotkanych wyzwaniach.
  - Ostateczna redakcja raportów w Jupyter Notebooks.
  - Podział slajdów i przygotowanie do obrony projektu.

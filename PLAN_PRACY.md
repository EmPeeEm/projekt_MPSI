# 📋 Plan Pracy i Podział Ról — Projekt MPSI

Niniejszy dokument opisuje podział odpowiedzialności w dwuosobowym zespole projektowym oraz przedstawia szczegółowy harmonogram (roadmapę) realizacji poszczególnych faz projektu modelowania tematów w NLP.

---

## 👥 Podział ról w zespole

### 👤 Osoba 1: Data & Interpretability (Specjalista ds. Danych i Ewaluacji Semantycznej)
Odpowiada za początkową oraz końcową fazę przetwarzania informacji tekstowych pod kątem ich znaczenia lingwistycznego i interpretacji.

- ⚙️ **Przygotowanie potoku danych (Data Pipeline)**:
  - Import zbioru danych *20 Newsgroups*.
  - Implementacja czyszczenia i preprocessingu w module [text_prep.py](src/text_prep.py) (tokenizacja, lematyzacja, filtracja stop words).
- 📐 **Reprezentacja wektorowa**:
  - Konfiguracja i optymalizacja parametrów transformacji **TF-IDF** (np. zakresy n-gramów, progi częstotliwości min_df/max_df).
- 💬 **Analiza i interpretacja semantyczna**:
  - Implementacja algorytmu ekstrakcji najważniejszych słów (Top Words) dla każdego z wygenerowanych klastrów na podstawie centroidów k-means.
  - Ocena spójności semantycznej (semantic coherence) klastrów.
- 🎤 **Prezentacja projektu**:
  - Odpowiedzialność za przedstawienie pierwszej części projektu (wprowadzenie, przygotowanie danych, inżynieria cech).

---

### 👤 Osoba 2: Modeling & Visualization (Specjalista ds. Modelowania i Wizualizacji)
Odpowiada za matematyczną i obliczeniową część projektu, strojenie parametrów modeli oraz czytelną prezentację graficzną wyników grupowania.

- 🤖 **Modelowanie (k-means)**:
  - Implementacja procesu uczenia algorytmu **k-means** (k-średnich) w notebooku [02_kmeans_i_tsne.ipynb](notebooks/02_kmeans_i_tsne.ipynb).
- 📊 **Analiza liczby klastrów ($k$)**:
  - Przeprowadzenie analizy wpływu doboru hiperparametru $k$ na podział dokumentów (np. za pomocą metody łokcia - *Elbow Method*, współczynnika sylwetki - *Silhouette Score* lub miar czystości klastrów).
- 🗺️ **Wizualizacja t-SNE**:
  - Zastosowanie algorytmu **t-SNE** do redukcji wymiarowości wielowymiarowej przestrzeni TF-IDF do przestrzeni dwuwymiarowej.
  - Opracowanie czytelnych wykresów rozrzutu (Scatter Plots) z kolorowaniem punktów według przynależności do klastrów.
- 🎤 **Prezentacja projektu**:
  - Odpowiedzialność za zaprezentowanie drugiej części projektu (klasteryzacja, analiza hiperparametrów, redukcja wymiarowości i wnioski końcowe).

---

## 🗺️ Roadmapa Projektu (5 Etapów)

Poniższa lista kontrolna określa kroki niezbędne do ukończenia projektu:

- [x] **Etap 1: Inicjalizacja projektu i strukturyzacja**
  - Stworzenie repozytorium Git i podłączenie submodułów.
  - Przygotowanie struktury katalogów (`data/`, `notebooks/`, `src/`).
  - Stworzenie pliku `requirements.txt` z bazowymi bibliotekami oraz plików dokumentacyjnych (`README.md`, `INSTRUKCJA.md`, `PLAN_PRACY.md`).
- [ ] **Etap 2: Pobranie danych i Preprocessing (Pipeline Osoby 1)**
  - Pobranie zbioru *20 Newsgroups* z biblioteki `scikit-learn`.
  - Stworzenie funkcji czyszczących tekst (usuwanie nagłówków e-maili, znaków specjalnych, stop words, lematyzacja).
  - Wdrożenie wektoryzacji TF-IDF i zapisanie przetworzonej macierzy rzadkiej.
  - Zakończenie prac nad notebookiem [01_preprocessing_i_tfidf.ipynb](notebooks/01_preprocessing_i_tfidf.ipynb).
- [ ] **Etap 3: Algorytm k-means i dobór liczby klastrów (Pipeline Osoby 2)**
  - Implementacja algorytmu k-means dla różnych wartości $k$.
  - Generowanie wykresów bezwładności (Inertia) w celu wyznaczenia optymalnego $k$ metodą łokcia.
  - Ocena stabilności i jakości podziału.
- [ ] **Etap 4: Interpretacja klastrów oraz Wizualizacja t-SNE (Wspólna integracja)**
  - Wyodrębnienie indeksów słów o najwyższych wagach w centroidach dla każdego klastra (Osoba 1).
  - Uruchomienie t-SNE na zredukowanej przestrzeni cech (np. po wstępnym PCA) i wygenerowanie dwuwymiarowego wykresu klastrów (Osoba 2).
  - Integracja i weryfikacja kodu w notebooku [02_kmeans_i_tsne.ipynb](notebooks/02_kmeans_i_tsne.ipynb).
- [ ] **Etap 5: Podsumowanie, wnioski i przygotowanie prezentacji**
  - Opisanie interpretacji tematów (np. Klaster 1: sport, Klaster 2: medycyna itp.).
  - Sformułowanie wniosków końcowych dotyczących ograniczeń k-means i reprezentacji TF-IDF w zadaniach NLP.
  - Przygotowanie ostatecznego konspektu prezentacji studenckiej oraz podziału slajdów.

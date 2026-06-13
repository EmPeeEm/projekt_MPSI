# 🛠️ Instrukcja Uruchomienia Projektu Lokalnie

Niniejsza instrukcja krok po kroku opisuje proces przygotowania środowiska lokalnego, instalacji zależności, uruchomienia eksperymentów w Jupyter Notebook oraz startu interaktywnej aplikacji Streamlit.

---

## 📋 Wymagania wstępne

Upewnij się, że na swoim komputerze masz zainstalowane następujące narzędzia:
- **Git** (do kontroli wersji)
- **Python** w wersji **3.10** lub nowszej
- Menedżer pakietów **pip**

---

## 🚀 Uruchomienie projektu krok po kroku

### Krok 1: Klonowanie repozytorium
Pobierz repozytorium na swój dysk lokalny za pomocą polecenia `git clone` w terminalu:

```bash
git clone https://github.com/EmPeeEm/projekt_MPSI.git
cd projekt_MPSI
```

---

### Krok 2: Tworzenie i aktywacja środowiska wirtualnego
Zalecamy użycie dedykowanego środowiska wirtualnego, aby uniknąć konfliktów z globalnymi bibliotekami w systemie.

1. **Utwórz środowisko wirtualne** o nazwie `.venv`:
   ```bash
   python3 -m venv .venv
   ```

2. **Aktywuj środowisko**:
   - **macOS / Linux**:
     ```bash
     source .venv/bin/activate
     ```
   - **Windows** (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - **Windows** (Command Prompt):
     ```cmd
     .venv\Scripts\activate.bat
     ```

Po prawidłowej aktywacji na początku linii poleceń w terminalu powinieneś zobaczyć oznaczenie `(.venv)`.

---

### Krok 3: Instalacja zależności
Zaktualizuj menedżer pakietów `pip`, a następnie zainstaluj wszystkie wymagane biblioteki (`numpy`, `pandas`, `scikit-learn`, `matplotlib`, `streamlit`, `notebook`):

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📓 Uruchomienie Jupyter Notebook (Raporty i Eksperymenty)

Aby przeglądać i uruchamiać notebooki z eksperymentami, uruchom serwer Jupyter:

```bash
jupyter notebook
```

W przeglądarce otworzy się panel Jupyter. Przejdź do folderu `notebooks/` i uruchom:
1. 📓 [01_preprocessing_i_tfidf.ipynb](notebooks/01_preprocessing_i_tfidf.ipynb) — w celu weryfikacji pipeline'u czyszczenia danych i wektoryzacji.
2. 📓 [02_kmeans_i_tsne.ipynb](notebooks/02_kmeans_i_tsne.ipynb) — w celu uruchomienia samodzielnej implementacji k-means, analizy doboru klastrów, redukcji t-SNE i zapoznania się z analizą ograniczeń.

---

## 🖥️ Uruchomienie Aplikacji Streamlit (Interaktywny Dashboard)

Projekt oferuje interaktywny panel webowy do wizualizacji wyników i dokumentów w czasie rzeczywistym. Aby go uruchomić, wpisz w terminalu:

```bash
streamlit run app.py
```

Aplikacja otworzy się automatycznie w przeglądarce pod adresem `http://localhost:8501`. Umożliwia ona dynamiczne zmienianie liczby klastrów, przeglądanie "top słów" dla tematów oraz filtrowanie dokumentów.

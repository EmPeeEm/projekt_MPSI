# 🛠️ Instrukcja Uruchomienia Projektu Lokalnie

Niniejsza instrukcja krok po kroku opisuje proces przygotowania środowiska lokalnego oraz uruchomienia kodu i notebooków Jupyter w celu reprodukcji wyników modelowania tematów.

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
Zaktualizuj menedżer pakietów `pip`, a następnie zainstaluj wszystkie wymagane biblioteki zdefiniowane w pliku `requirements.txt`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Krok 4: Pobranie modeli lingwistycznych (opcjonalnie)
Jeżeli w projekcie do lematyzacji wykorzystywane są dodatkowe zasoby biblioteki `nltk` lub model językowy `spaCy`, należy je jednorazowo pobrać:

```bash
# Dla NLTK (przykładowo stop words i punktuatory):
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"

# Dla spaCy (jeśli używany jest model angielski en_core_web_sm):
python -m spacy download en_core_web_sm
```

---

### Krok 5: Uruchomienie Jupyter Notebook
Po pomyślnej instalacji pakietów możesz uruchomić serwer Jupyter Notebook:

```bash
jupyter notebook
```

Po uruchomieniu tego polecenia w przeglądarce automatycznie otworzy się panel Jupyter. Przejdź do folderu `notebooks/` i otwórz w odpowiedniej kolejności:
1. 📓 [01_preprocessing_i_tfidf.ipynb](notebooks/01_preprocessing_i_tfidf.ipynb) — w celu zapoznania się z pipeline przygotowania danych.
2. 📓 [02_kmeans_i_tsne.ipynb](notebooks/02_kmeans_i_tsne.ipynb) — w celu uruchomienia klasteryzacji i analizy wyników.

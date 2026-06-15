import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Funkcja pomocnicza do pobrania niezbędnych zasobów NLTK
# Uruchom ją raz przed pierwszym użyciem
def download_nltk_resources():
    print("Pobieranie zasobów NLTK...")
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    print("Zasoby pobrane!")

def clean_text(text):
    """
    Wstępne czyszczenie tekstu (wyrażenia regularne).
    """
    # Zmiana na małe litery
    text = text.lower()
    
    # Usuwanie adresów e-mail (częste w 20 Newsgroups)
    text = re.sub(r'\S+@\S+', '', text)
    
    # Usuwanie znaków nowej linii i tabulacji
    text = re.sub(r'[\r\n\t]+', ' ', text)
    
    # Pozostawienie tylko liter (usuwanie cyfr i znaków interpunkcyjnych)
    text = re.sub(r'[^a-z\s]', ' ', text)
    
    # Usuwanie podwójnych/wielokrotnych spacji
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def preprocess_document(text):
    """
    Główna funkcja przetwarzająca pojedynczy dokument.
    Wykonuje czyszczenie, tokenizację, filtrację stop words i lematyzację.
    """
    # 1. Czyszczenie tekstu
    cleaned_text = clean_text(text)
    
    # 2. Tokenizacja (podział na słowa)
    tokens = word_tokenize(cleaned_text)
    
    # 3. Inicjalizacja narzędzi NLTK i rozszerzenie o własne stop words
    stop_words = set(stopwords.words('english'))
    custom_stop_words = {
        'would', 'know', 'think', 'people', 'use', 'time', 'anyone', 
        'please', 'thanks', 'mail', 'like', 'email', 'advance', 'get', 
        'one', 'say', 'go', 'think', 'good', 'well', 'make', 'right', 'see'
    }
    stop_words.update(custom_stop_words)
    lemmatizer = WordNetLemmatizer()
    
    # 4. Filtracja stop words, lematyzacja i odrzucenie bardzo krótkich słów
    processed_tokens = []
    for word in tokens:
        if word not in stop_words and len(word) > 2: # odrzucamy też słowa 1- i 2-literowe
            lemma = lemmatizer.lemmatize(word)
            processed_tokens.append(lemma)
            
    # Zwracamy połączony string (wymagane przez TfidfVectorizer w scikit-learn)
    return " ".join(processed_tokens)

def preprocess_corpus(corpus):
    """
    Funkcja przyjmująca listę dokumentów i zwracająca listę przetworzonych dokumentów.
    """
    return [preprocess_document(doc) for doc in corpus]

# Jeśli plik zostanie uruchomiony bezpośrednio, pobierze zasoby
if __name__ == "__main__":
    download_nltk_resources()
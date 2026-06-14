import numpy as np

def get_top_words(vectorizer, centroids, n_words=10):
    """
    Wyciąga najważniejsze słowa (słowa kluczowe) dla każdego klastra na podstawie 
    wartości współrzędnych w centroidach (wagi TF-IDF).
    
    Parametry:
    - vectorizer: Dopasowany obiekt TfidfVectorizer z scikit-learn.
    - centroids: Tablica NumPy zawierająca centroidy klastrów o kształcie (n_clusters, n_features).
    - n_words (int): Liczba słów kluczowych do wyciągnięcia dla każdego klastra.
    
    Zwraca:
    - dict: Słownik, gdzie kluczem jest indeks klastra, a wartością lista najpopularniejszych słów.
    """
    # Pobranie słownika słów z wektoryzatora
    feature_names = np.array(vectorizer.get_feature_names_out())
    top_words_per_cluster = {}
    
    for i, centroid in enumerate(centroids):
        # Sortowanie indeksów wag rosnąco, wybór n_words największych i odwrócenie kolejności (malejąco)
        top_indices = np.argsort(centroid)[-n_words:][::-1]
        top_words = feature_names[top_indices].tolist()
        top_words_per_cluster[i] = top_words
        
    return top_words_per_cluster

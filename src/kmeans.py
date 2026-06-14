import numpy as np

class KMeans:
    """
    Własna implementacja algorytmu KMeans (k-średnich) przy użyciu NumPy.
    Zgodna z interfejsem scikit-learn (fit, predict, transform).
    """
    def __init__(self, n_clusters=8, init='k-means++', max_iter=300, tol=1e-4, random_state=None):
        """
        Inicjalizacja parametrów algorytmu.
        
        Parametry:
        - n_clusters (int): Liczba klastrów (tematów).
        - init (str): Metoda inicjalizacji centroidów ('random' lub 'k-means++').
        - max_iter (int): Maksymalna liczba iteracji w pętli głównej.
        - tol (float): Tolerancja zbieżności kryterium stopu (przesunięcie centroidów).
        - random_state (int/None): Ziarno generatora liczb losowych.
        """
        self.n_clusters = n_clusters
        self.init = init
        self.max_iter = max_iter
        self.tol = tol
        self.random_state = random_state
        
        # Atrybuty wyjściowe (zbieżne z nazewnictwem scikit-learn)
        self.cluster_centers_ = None  # Centroidy klastrów
        self.labels_ = None           # Etykiety przypisane do każdego punktu
        self.inertia_ = None          # Suma kwadratów odległości od centroidów (SSE)
        self.n_iter_ = None           # Liczba wykonanych iteracji

    def _init_centroids(self, X):
        """
        Inicjalizacja centroidów zgodnie z wybraną strategią ('random' lub 'k-means++').
        """
        n_samples, n_features = X.shape
        rng = np.random.default_rng(self.random_state)
        
        if self.init == 'random':
            # Losowy wybór n_clusters unikalnych indeksów punktów z danych wejściowych
            idx = rng.choice(n_samples, self.n_clusters, replace=False)
            return X[idx].copy()
            
        elif self.init == 'k-means++':
            centroids = np.empty((self.n_clusters, n_features))
            
            # 1. Pierwszy centroid losowany jednostajnie ze zbioru danych
            first_idx = rng.choice(n_samples)
            centroids[0] = X[first_idx]
            
            # Tablica przechowująca najmniejsze kwadraty odległości od dotychczasowych centroidów
            min_sq_dists = np.full(n_samples, np.inf)
            
            for i in range(1, self.n_clusters):
                # 2. Obliczamy odległości wszystkich punktów od ostatnio wybranego centroidu
                last_centroid = centroids[i - 1]
                
                # Wydajna wektoryzacja odległości: ||x - c||^2 = ||x||^2 - 2<x, c> + ||c||^2
                X_sq = np.sum(X**2, axis=1)
                c_sq = np.sum(last_centroid**2)
                dot_prod = np.dot(X, last_centroid)
                dists = np.maximum(X_sq - 2 * dot_prod + c_sq, 0.0)
                
                # Aktualizujemy najmniejsze odległości kwadratowe
                min_sq_dists = np.minimum(min_sq_dists, dists)
                
                # 3. Wybieramy kolejny centroid z prawdopodobieństwem proporcjonalnym do D(x)^2
                sum_sq_dists = np.sum(min_sq_dists)
                if sum_sq_dists == 0.0:
                    prob = np.ones(n_samples) / n_samples
                else:
                    prob = min_sq_dists / sum_sq_dists
                
                next_idx = rng.choice(n_samples, p=prob)
                centroids[i] = X[next_idx]
                
            return centroids
        else:
            raise ValueError("Parametr init musi przyjmować wartość 'random' lub 'k-means++'")

    def fit(self, X):
        """
        Dopasowanie modelu do danych X (uczenie algorytmu).
        
        Parametry:
        - X (array-like/sparse matrix): Dane wejściowe o wymiarach (n_samples, n_features)
        """
        # Konwersja macierzy rzadkiej (TF-IDF) na gęstą tablicę NumPy
        if hasattr(X, "toarray"):
            X = X.toarray()
        else:
            X = np.asarray(X)
            
        n_samples, n_features = X.shape
        
        if n_samples < self.n_clusters:
            raise ValueError("Liczba próbek (n_samples) nie może być mniejsza niż liczba klastrów (n_clusters).")
            
        # Inicjalizacja centroidów
        self.cluster_centers_ = self._init_centroids(X)
        
        # Obliczenie kwadratów norm punktów X do triku macierzowego odległości
        X_sq = np.sum(X**2, axis=1, keepdims=True)
        
        self.n_iter_ = 0
        for iteration in range(self.max_iter):
            self.n_iter_ = iteration + 1
            
            # KROK 1: Przypisanie punktów do najbliższego centroidu
            # ||X - C||^2 = ||X||^2 - 2 * X.C^T + ||C||^2
            C_sq = np.sum(self.cluster_centers_**2, axis=1)
            dot_prod = np.dot(X, self.cluster_centers_.T)
            dists = np.maximum(X_sq - 2 * dot_prod + C_sq, 0.0)
            
            labels = np.argmin(dists, axis=1)
            
            # KROK 2: Obliczenie nowych centroidów jako średnich z przypisanych punktów
            new_centers = np.empty_like(self.cluster_centers_)
            for j in range(self.n_clusters):
                members = X[labels == j]
                if len(members) > 0:
                    new_centers[j] = np.mean(members, axis=0)
                else:
                    # Jeśli klaster jest pusty, losujemy nowy centroid ze zbioru danych
                    rng = np.random.default_rng(self.random_state)
                    new_centers[j] = X[rng.choice(n_samples)]
            
            # KROK 3: Sprawdzenie warunku stopu (zbieżność)
            center_shift = np.sum((self.cluster_centers_ - new_centers) ** 2)
            self.cluster_centers_ = new_centers
            
            if center_shift < self.tol:
                break
                
        # Zapisanie ostatecznych etykiet oraz inercji (SSE)
        self.labels_ = labels
        C_sq = np.sum(self.cluster_centers_**2, axis=1)
        dot_prod = np.dot(X, self.cluster_centers_.T)
        final_dists = np.maximum(X_sq - 2 * dot_prod + C_sq, 0.0)
        self.inertia_ = np.sum(np.min(final_dists, axis=1))
        
        return self

    def predict(self, X):
        """
        Predykcja klastrów dla nowych danych X.
        """
        if hasattr(X, "toarray"):
            X = X.toarray()
        else:
            X = np.asarray(X)
            
        X_sq = np.sum(X**2, axis=1, keepdims=True)
        C_sq = np.sum(self.cluster_centers_**2, axis=1)
        dot_prod = np.dot(X, self.cluster_centers_.T)
        dists = np.maximum(X_sq - 2 * dot_prod + C_sq, 0.0)
        return np.argmin(dists, axis=1)

    def transform(self, X):
        """
        Transformacja danych do przestrzeni odległości od centroidów.
        Zwraca macierz o wymiarach (n_samples, n_clusters).
        """
        if hasattr(X, "toarray"):
            X = X.toarray()
        else:
            X = np.asarray(X)
            
        X_sq = np.sum(X**2, axis=1, keepdims=True)
        C_sq = np.sum(self.cluster_centers_**2, axis=1)
        dot_prod = np.dot(X, self.cluster_centers_.T)
        dists = np.maximum(X_sq - 2 * dot_prod + C_sq, 0.0)
        return np.sqrt(dists)

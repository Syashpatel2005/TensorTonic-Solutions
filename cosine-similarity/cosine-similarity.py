import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)
    if (a==0).all() or (b==0).all():
        return 0
    c = np.sum(a**2)**0.5
    d = np.sum(b**2)**0.5
    return np.dot(a,b)/ (c * d)
    pass
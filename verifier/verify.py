import numpy as np

def load_signal(path):
    return np.loadtxt(path)

def compare_signals(sig1, sig2):
    # Basic Euclidean distance (simple demo only)
    distance = np.linalg.norm(sig1 - sig2)

    # Static threshold (NOT your real one)
    if distance < 500:
        return "AUTHENTIC"
    else:
        return "REJECT"
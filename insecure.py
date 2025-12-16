try:
    import cPickle as pickle
except ImportError:
    import pickle

def load_data(path):
    with open(path, "rb") as f:
        return pickle.load(f)

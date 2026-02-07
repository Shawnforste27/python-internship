import pandas as pd

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load_csv(self):
        df = pd.read_csv(self.path)
        print("✅ Data loaded:", df.shape)
        return df

import pandas as pd

# Example function to load and preprocess data
def load_and_preprocess(file_path):
    # Read data
    data = pd.read_csv(file_path)
    
    # Preprocess (example: lowercasing text)
    data["text"] = data["text"].str.lower()
    
    return data

if __name__ == "__main__":
    # Example usage
    train_data = load_and_preprocess("../data/train.csv")
    print(train_data.head())

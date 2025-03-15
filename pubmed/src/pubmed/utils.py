import pandas as pd

def save_to_csv(data, filename):
    """Saves data to a CSV file using pandas."""
    if not data:
        print("No data to save.")
        return

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

import pandas as pd

def load_data(file_name):
    """Load CSV file into dataframe"""
    try:
        df = pd.read_csv(file_name)
        print("Data Loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
def process_data(dataframe):
    """Simple processing show summary"""
    print("\n ---Data Summary---")
    print(dataframe.describe())
# a = 7
#print(a)
# This part runs only if this script is executed directly

if __name__ == '__main__':
    filename = "NIFTY50.csv"
    data =load_data(filename)
    if data is not None:
        process_data(data)
#print()

#print("Hello World my name is Harry")

def printhar(string):
    return f"Ye string bohot important he {string}"

def add(num1,num2):
    return num1+num2+5

print("the name is", __name__)

if __name__ == '__main__':
    print(printhar("Harry"))
    print(add(5, 10))

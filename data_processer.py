import pandas as pd

def process_csv(file_path):
    try:
        # Read CSV into a DataFrame
        df = pd.read_csv(file_path, on_bad_lines='skip')

        # Process the data (replace this with your actual processing logic)
        # For example, let's print the contents of the DataFrame
        print(df)

    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    csv_file_path = "data.csv"  # Update this with your actual CSV file path
    process_csv(csv_file_path)

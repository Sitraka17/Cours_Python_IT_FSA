import pandas as pd
import numpy as np

def analyze_columns(dataframe):
    analysis_results = {}
    
    for column in dataframe.columns:
        column_data = dataframe[column]
        column_type = column_data.dtype
        
        analysis = {
            "data_type": str(column_type),
            "non_null_count": column_data.count(),
            "null_count": column_data.isnull().sum(),
            "unique_values": column_data.nunique()
        }
        
        if np.issubdtype(column_type, np.number):
            analysis.update({
                "min": column_data.min(),
                "max": column_data.max(),
                "mean": column_data.mean(),
                "median": column_data.median(),
                "std_dev": column_data.std()
            })
        elif column_type == 'object' or column_type == 'string':
            analysis.update({
                "min_length": column_data.str.len().min(),
                "max_length": column_data.str.len().max(),
                "sample_values": column_data.sample(min(5, len(column_data))).tolist()
            })
        
        analysis_results[column] = analysis
    
    return analysis_results

def print_analysis(analysis_results):
    for column, analysis in analysis_results.items():
        print(f"\nColumn: {column}")
        for key, value in analysis.items():
            print(f"  {key}: {value}")

# Example usage
if __name__ == "__main__":
    # Load your data (replace this with your actual data loading method)
    df = pd.read_csv("your_data.csv")
    
    # Analyze columns
    results = analyze_columns(df)
    
    # Print results
    print_analysis(results)

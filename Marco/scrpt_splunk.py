import json
import pandas as pd

# Pour palier le pandas on fait une méthode plus basique: on crée une liste vide qu'on remplira. 
extracted_data = []

# Open the JSON et lecture ligne par ligne 
with open('INC0438830.json', 'r') as f:
    for line in f:
        if line.strip():  # Ensure the line is not vide
            try:
                # Parse the JSON line
                data = json.loads(line)
                
                # Extract the necessary columns
                extracted_data.append({
                    '_time': data['result']['_time'],
                    'accountNumber': data['result']['accountNumber']
                })
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

# Convert the extracted data into a DataFrame
df = pd.DataFrame(extracted_data)

# Export the DataFrame to a text file
df.to_csv('extracted_data.txt', sep='\t', index=False)

print("Data successfully extracted and saved to extracted_data.txt.")

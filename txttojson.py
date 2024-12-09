import json 
import os 


output_folder = "output_folder/"
dataset = []

for text_file in os.listdir(output_folder):
  if text_file.endswith(".txt"):
    file_path = os.path.join(output_folder, text_file)
    with open(file_path, "r", encoding="utf-8") as f:
      content = f.read()
      dataset.append({"filename": text_file, "content": content})

# Save the dataset as JSON
with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(dataset, f, ensure_ascii=False, indent=4)

print("Dataset saved to dataset.json")
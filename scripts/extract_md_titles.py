import os
import json

docs_dir = "C:/data/docs/"
output_file = os.path.join(docs_dir, "index.json")
index = {}

# Walk through all subdirectories
for root, _, files in os.walk(docs_dir):
    for filename in files:
        if filename.endswith(".md"):
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, docs_dir)

            # Read the first H1 heading
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if line.startswith("# "):  # H1 heading
                        index[relative_path] = line[2:]
                        break  # Stop at first H1

# Save to JSON
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(index, json_file, indent=4)

print(f"✅ Generated {output_file} with {len(index)} entries")
